      ******************************************************************
      * Author:
      * Date:
      * Purpose: Ler arquivo gerado e formatar para tamanho fixo
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FLORICULTURA_ARQUIVO.
      * 
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
          FILE-CONTROL.
              SELECT ARQUIVO ASSIGN TO CAMINHO-ARQUIVO
              ORGANIZATION IS LINE SEQUENTIAL
              FILE STATUS IS FS-ARQUIVO.
      * 
       DATA DIVISION.
       FILE SECTION.
         FD ARQUIVO.
         01 REGISTRO         PIC X(80).
      * 
       WORKING-STORAGE SECTION.
       01  CAMINHO-ARQUIVO PIC X(100) VALUE
           'C:\Users\WIN 11\Floricultura\Floricultura-1' &
                   '\scripts\tabela_plantas.txt'.
                   
       01  STATUS-ARQUIVO.
           05 FS-ARQUIVO       PIC 9(02).
       
       01  WS-ARQUIVO          PIC X(80).          
      *     
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM ABRE-ARQUIVO.
           PERFORM LE-ARQUIVO.
           PERFORM FECHA-ARQUIVO.
           STOP RUN.
           
           
          ABRE-ARQUIVO.
               OPEN INPUT ARQUIVO.
               IF FS-ARQUIVO NOT = 00
                   DISPLAY 'ERRO AO ABRIR O ARQUIVO. STATUS: 'FS-ARQUIVO
                   STOP RUN
               ELSE
                   DISPLAY 'ARQUIVO ABERTO COM SUCESSO!'.
               
          LE-ARQUIVO.
               PERFORM UNTIL FS-ARQUIVO NOT = 00
                   READ WS-ARQUIVO INTO WS-REGISTRO
                   AT END
                       
                   UNSTRING WS-ARQUIVO
                       DELIMITED BY ';'
                       INTO WS-REGISTRO
                   END-UNSTRING    
               END-PERFORM.    
               
          FECHA-ARQUIVO.
               CLOSE ARQUIVO.
               IF FS-ARQUIVO NOT = 00
                 DISPLAY 'ERRO AO FECHAR O ARQUIVO. STATUS: ' FS-ARQUIVO
               ELSE
                 DISPLAY 'ARQUIVO FECHADO COM SUCESSO.'.
               
               
       END PROGRAM FLORICULTURA_ARQUIVO.

