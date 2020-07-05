#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <jansson.h>
#include <stdbool.h>

const char *command_getSoalJawabanTP = "curl -s -X POST https://daskomlab.com/api/getTp/%s/%d | jq -c '[ .all_tp | .[] | select( .isProgram == 1 ) | {soal: .soal, jawaban: .jawaban} ]'";
const char *command_indentAndShowCode = "echo '%s' > tmp ; astyle -q tmp ; rm tmp.orig ; cat tmp ; rm tmp";
const char *command_writeAndExecute = "echo '%s' > tmp.c ; gcc -o tmp tmp.c";
const char *command_cleanAllTheThings = "[ -f tmp ] && rm tmp ; [ -f tmp.c ] && rm tmp.c";

char *send_command (char *input, bool showOutput) {

    FILE *fd;
    fd = popen(input, "r");
    if (!fd) return "nope";
 
    char   buffer[256];
    size_t chread;
    /* String to store entire command contents in */
    size_t comalloc = 256;
    size_t comlen   = 0;
    char  *comout   = malloc(comalloc);
 
    /* Use fread so binary data is dealt with correctly */
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

    // Dont forget to free the malloc (the meme stops here :v)
    // free(comout);

    pclose(fd);
    return comout;
}

/**
 * root = json data
 * output type = 1 (soal) | 2 (jawaban) | 3 (running praktikan's code)
 * soal id = id of soal
 * 
 * return int
 */
int showJsonOutput (json_t *root, int output_type, int soal_id) {

    size_t i;

    for (i = 0; i < json_array_size(root); i++) {
        json_t *data, *soal, *jawaban;

        data = json_array_get(root, i);
        if (!json_is_object(data)) {
            fprintf(stderr, "error: json data %d is not an object\n", (int)(i + 1));
            json_decref(root);
            return 1;
        }

        soal = json_object_get(data, "soal");
        if (!json_is_string(soal)) {
            fprintf(stderr, "error: json %d: soal is not a string\n", (int)(i + 1));
            json_decref(root);
            return 1;
        }

        jawaban = json_object_get(data, "jawaban");
        if (!json_is_string(jawaban)) {
            fprintf(stderr, "error: json %d: jawaban is not an object\n", (int)(i + 1));
            json_decref(root);
            return 1;
        }

        switch (output_type) {
            case 1:
                printf("===========\n");
                printf("[%d] %s\n\n", (int)(i + 1), json_string_value(soal));
                break;

            case 2:
                if(soal_id == (int)(i + 1)) {

                    char command[(strlen(command_indentAndShowCode) - 2) + 2056];
                    sprintf(command, command_indentAndShowCode, json_string_value(jawaban));

                    printf("==SHOWING PRAKTIKAN'S CODE==\n==(Alert: careful, it's usually bad codes, please forgive them and dont make the code as a meme)==\n\n");
                    char *code = send_command(command, true);
                    free(code);
                }
                break;

            case 3:
                if(soal_id == (int)(i + 1)) {

                    char command1[(strlen(command_writeAndExecute) - 2) + 2056];
                    sprintf(command1, command_writeAndExecute, json_string_value(jawaban));

                    printf("==COMPILING PRAKTIKAN'S CODE==\n\n");
                    char *compile = send_command(command1, true);
                    free(compile);

                    printf("==RUNNING PRAKTIKAN'S CODE==\n\n");
                    system("./tmp");

                    char command2[strlen(command_cleanAllTheThings) + 1];
                    sprintf(command2, command_cleanAllTheThings);
                    char *clean = send_command(command2, true);
                    free(clean);
                }
                break;
            
            default:
                break;
        }
    }

    getchar();
    getchar();
    return 0;
}

int main () {

    char input[11];
    
    printf("Nim = ");
    fgets(input, 11, stdin);
    input[strcspn(input, "\r\n")] = 0;
    
    printf(
"\n\
1. Instalasi IDE\n\
2. Tipe Data\n\
3. Percabangan\n\
4. Perulangan\n\
5. Fungsi\n\
11. Array & array of string\n\
12. Sorting\n\
13. Searching\n\
14. Algoritma Rekursif\n\
15. File Sekuensial\n\
"   );

    int modulPil;
    printf("Pilih Modul = ");
    scanf("%d", &modulPil);
    fflush(stdin);

    char command[(strlen(command_getSoalJawabanTP) - 4) + 14];
    sprintf(command, command_getSoalJawabanTP, input, modulPil);
    
    char *output = send_command(command, false);

    json_t *jsonData;
    json_error_t error;

    jsonData = json_loads(output, 0, &error);
    free(output);

    bool stillRunning = true;
    while(stillRunning) {
        
        system("clear");

        printf("-----------------------\n");
        printf("| MENU                |\n");
        printf("| 1. Lihat soal       |\n");
        printf("| 2. Lihat jawaban    |\n");
        printf("| 3. Jalankan jawaban |\n");
        printf("| 4. Keluar aplikasi  |\n");
        printf("-----------------------\n");
        printf("Masukkan pilihan = ");
        
        int pil, jawaban_pil;
        scanf("%d", &pil);
        fflush(stdin);

        switch (pil) {
            case 1:
                showJsonOutput(jsonData, 1, -1);
                break;

            case 2:
                printf("Masukkan no soal = ");
                scanf("%d", &jawaban_pil);
                fflush(stdin);  
                showJsonOutput(jsonData, 2, jawaban_pil);
                break;

            case 3:
                printf("Masukkan no soal = ");
                scanf("%d", &jawaban_pil);
                fflush(stdin);  
                showJsonOutput(jsonData, 3, jawaban_pil);
                break;

            case 4:
                stillRunning = false;
                break;
            
            default:
                break;
        }
    }

    json_decref(jsonData);
    return 0;
}