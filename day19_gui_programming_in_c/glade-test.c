#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <gtk/gtk.h>
#include <gtk/gtkx.h>

GtkWidget  *window;
GtkWidget  *fixed;
GtkWidget  *button;
GtkBuilder *builder;

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);

    builder = gtk_builder_new_from_file ("glade-test.glade");
    window = GTK_WIDGET(gtk_builder_get_object(builder, "window"));

    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);
    gtk_builder_connect_signals(builder, NULL);

    fixed = GTK_WIDGET(gtk_builder_get_object(builder, "fixed"));
    button = GTK_WIDGET(gtk_builder_get_object(builder, "button"));

    gtk_widget_show(window);
    gtk_main();

    return 0;
}

void on_button1_clicked (GtkButton *b) {
    printf("Hello World");
}