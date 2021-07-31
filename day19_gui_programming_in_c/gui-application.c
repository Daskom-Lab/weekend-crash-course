/*
    install gtk and jansson first and the you can compile
    this program using below command

    gcc `pkg-config --cflags gtk+-3.0` -o code.bin gui-application.c `pkg-config --libs gtk+-3.0` `pkg-config --libs jansson` -rdynamic
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Use jansson lib to handle json parsing
#include <jansson.h>

// Use gtk lib to create the gui
#include <gtk/gtk.h>
#include <gtk/gtkx.h>

// Main Widget
GtkWidget  *window;
GtkWidget  *fixed;
GtkBuilder *builder;

// Controllable Widget
GtkWidget  *input_nim;
GtkWidget  *label_nim;
GtkWidget  *input_soal;
GtkWidget  *label_soal;
GtkWidget  *input_modul;
GtkWidget  *label_modul;

// Result Widget
GtkWidget  *input_tp_jawaban;
GtkWidget  *label_tp_soal;

// Command to get the json from the endpoint and parse it such that we only grab the "soal" and "jawaban" for "program" type of "soal"
const char *command_getSoalJawabanTP = "curl -s -X POST https://daskomlab.com/api/getTp/%s/%s | jq -c '[ .all_tp | .[] | select( .isProgram == 1 ) | {soal: .soal, jawaban: .jawaban} ]'";

// Command to indent the code and get the code content using cat command
const char *command_indentAndShowCode = "echo '%s' > tmp ; astyle -q tmp ; rm tmp.orig ; cat tmp ; rm tmp";

/**
 * Send command from a string to the operating system
 *
 * taken from https://rosettacode.org/wiki/Get_system_command_output#C
 * and tweaked for this program needs
 */
char *send_command (char *input, bool showOutput) {

    FILE *fd;
    fd = popen(input, "r");
    if (!fd) return "nope";

    char   buffer[256];
    size_t chread;

    // String to store entire command contents in
    size_t comalloc = 256;
    size_t comlen   = 0;
    char  *comout   = malloc(comalloc);

    // Use fread so binary data is dealt with correctly
    while ((chread = fread(buffer, 1, sizeof(buffer), fd)) != 0) {
        if (comlen + chread >= comalloc) {
            comalloc *= 2;
            comout = realloc(comout, comalloc);
        }
        memmove(comout + comlen, buffer, chread);
        comlen += chread;
    }

    // In case you want the output straightly to stdout
    if(showOutput)
        fwrite(comout, 1, comlen, stdout);

    // Dont forget to free after usage of this function output
    // free(comout);

    pclose(fd);
    return comout;
}

/**
 * Get json output
 *
 * root = json data
 * output type = 1 (soal) | 2 (jawaban) | 3 (running praktikan's code)
 * soal id = id of soal
 *
 * return int
 */
void showJsonOutput (json_t *root, int soal_id) {

    size_t i;

    // Iterate over all the json to get the desired content of "soal_id"
    for (i = 0; i < json_array_size(root); i++) {
        json_t *data, *soal, *jawaban;

        // Parse the root json to get the data with current iteration value
        data = json_array_get(root, i);

        // Error handling to check if "data" is a json object
        if (!json_is_object(data)) {
            fprintf(stderr, "error: json data %d is not an object\n", (int)(i + 1));
            json_decref(root);
            // TODO: show some error
        }

        // Parse the "soal" content from the parsed "data" json object
        soal = json_object_get(data, "soal");

        // Error handling to check if "soal" is a json string
        if (!json_is_string(soal)) {
            fprintf(stderr, "error: json %d: soal is not a string\n", (int)(i + 1));
            json_decref(root);
            // TODO: show some error
        }

        // Parse the "jawaban" content from the parsed "data" json object
        jawaban = json_object_get(data, "jawaban");

        // Error handling to check if "jawaban" is a json string
        if (!json_is_string(jawaban)) {
            fprintf(stderr, "error: json %d: jawaban is not an object\n", (int)(i + 1));
            json_decref(root);
            // TODO: show some error
        }

        // Check if the current iteration value match with the desired "soal_id"
        if(soal_id == (int)(i + 1)) {

            // Create a command variable to put the resulting command + the value from
            // the parsed "jawaban" json string
            char command[(strlen(command_indentAndShowCode) - 2) + 2056];
            sprintf(command, command_indentAndShowCode, json_string_value(jawaban));

            // Send the command to the OS and get the output
            char *code = send_command(command, false);

            // Set `input_tp_jawaban` to the code that is generated from the command result
            GtkTextBuffer *buffer = gtk_text_view_get_buffer(GTK_TEXT_VIEW(input_tp_jawaban));
            gtk_text_buffer_set_text(buffer, (const gchar* ) code, -1);

            // Set `label_tp_soal` label to the corresponding "soal"
            gtk_label_set_text(GTK_LABEL(label_tp_soal), (const gchar* ) json_string_value(soal));

            // Free the resource allocation for command output
            free(code);
            break;
        }
    }
}

int main(int argc, char *argv[]) {

    /************************ Setups Initialization ******************************/

    // Gtk intialization
    gtk_init(&argc, &argv);

    // Parse the glade generated file to create an equivalent gtk gui tree
    builder = gtk_builder_new_from_file ("gui-application.glade");

    // Grab the main window from the parsed gui tree to a variable for later use
    window = GTK_WIDGET(gtk_builder_get_object(builder, "window"));

    // Connect the "destroy" signal to the main window and to the gtk_main_quit callback
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    // Build every signal and connection from the parsed gui tree
    gtk_builder_connect_signals(builder, NULL);

    // Grab the "fixed" ui component from the parsed gui tree to a variable for later use
    fixed = GTK_WIDGET(gtk_builder_get_object(builder, "fixed"));

    /***************************************************************************/


    /************************ Controllable Widget ******************************/

    // Grab the "input_nim" ui component from the parsed gui tree to a variable for later use
    input_nim = GTK_WIDGET(gtk_builder_get_object(builder, "input_nim"));
    // Grab the "label_nim" ui component from the parsed gui tree to a variable for later use
    label_nim = GTK_WIDGET(gtk_builder_get_object(builder, "label_nim"));
    // Grab the "input_soal" ui component from the parsed gui tree to a variable for later use
    input_soal = GTK_WIDGET(gtk_builder_get_object(builder, "input_soal"));
    // Grab the "label_soal" ui component from the parsed gui tree to a variable for later use
    label_soal = GTK_WIDGET(gtk_builder_get_object(builder, "label_soal"));
    // Grab the "input_modul" ui component from the parsed gui tree to a variable for later use
    input_modul = GTK_WIDGET(gtk_builder_get_object(builder, "input_modul"));
    // Grab the "label_modul" ui component from the parsed gui tree to a variable for later use
    label_modul = GTK_WIDGET(gtk_builder_get_object(builder, "label_modul"));

    // Result Widget
    // Grab the "input_tp_jawaban" ui component from the parsed gui tree to a variable for later use
    input_tp_jawaban = GTK_WIDGET(gtk_builder_get_object(builder, "input_tp_jawaban"));
    // Grab the "label_tp_soal" ui component from the parsed gui tree to a variable for later use
    label_tp_soal = GTK_WIDGET(gtk_builder_get_object(builder, "label_tp_soal"));

    /***************************************************************************/

    // Show the main window widget and everything inside of it
    gtk_widget_show(window);

    // Run the gtk main event loop
    gtk_main();

    return 0;
}

void on_button1_clicked(GtkButton *b) {
    // Get the text inputted in the `input_nim` and `input_modul`
    const gchar* nim = gtk_entry_get_text(GTK_ENTRY(input_nim));
    const gchar* modul = gtk_entry_get_text(GTK_ENTRY(input_modul));

    // Create a command variable to put the resulting command
    char command[(strlen(command_getSoalJawabanTP) - 4) + 14];
    sprintf(command, command_getSoalJawabanTP, nim, modul);

    // Get the result of `getSoalJawabanTP` command
    char *output = send_command(command, false);

    // Create a variable to store the resulting json data
    json_t *jsonData;
    json_error_t error;

    // Store resulting json data to the variable by parsing it
    // using the `json_loads` function
    jsonData = json_loads(output, 0, &error);

    // Print error on the json parser if any
    if(!jsonData)
        printf("JSON Error on line %d: %s\n\n", error.line, error.text);

    // Free the resource allocation for command output
    free(output);

    // Get the text inputted in the `input_soal`
    const gchar* soal = gtk_entry_get_text(GTK_ENTRY(input_soal));
    int soal_id = atoi(soal);

    // Get json output for the corresponding `soal_id`
    showJsonOutput(jsonData, soal_id);

    // Free the jsonData resource allocation
    json_decref(jsonData);
}