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
       CONFIGURATION SECTION.    
           SPECIAL-NAMES.
               DECIMAL-POINT IS COMMA.
      * 
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
           'C:\Users\tihso\OneDrive\Área de Trabalho\Floricultura' &
               '\Floricultura-7\scripts\tabela_plantas.txt'.
                   
       01  STATUS-ARQUIVO.
           05 FS-ARQUIVO       PIC 9(02).
       
       01  WS-ARQUIVO          PIC X(80).
       
       01  WS-REGISTRO.
           05 WS-ID            PIC 9(01).
           05 WS-NOME          PIC X(30).
           05 WS-PRECO         PIC 9(8)V99.
           05 WS-PREFERENCIA   PIC X(41).
           
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
                   READ ARQUIVO INTO WS-ARQUIVO
                   AT END
                       MOVE 99 TO FS-ARQUIVO
                   NOT AT END
                       PERFORM UNSTRING-ARQUIVO
                       PERFORM MOSTRA-ARQUIVO
               END-PERFORM.    
           
          UNSTRING-ARQUIVO.
               UNSTRING WS-ARQUIVO
                   DELIMITED BY ';'
                   INTO WS-ID
                        WS-NOME
                        WS-PRECO
                        WS-PREFERENCIA
              END-UNSTRING.
           
          MOSTRA-ARQUIVO.
               DISPLAY '-------------------------------------------'
               DISPLAY 'WS-ARQUIVO: 'WS-ARQUIVO.
               DISPLAY 'ID: 'WS-ID.
               DISPLAY 'NOME: 'WS-NOME.
               DISPLAY 'PRECO: 'WS-PRECO.
               DISPLAY 'PREFERENCIA: 'WS-PREFERENCIA.
               
          FECHA-ARQUIVO.
               CLOSE ARQUIVO.
               IF FS-ARQUIVO NOT = 00
                 DISPLAY 'ERRO AO FECHAR O ARQUIVO. STATUS: ' FS-ARQUIVO
               ELSE
                 DISPLAY 'ARQUIVO FECHADO COM SUCESSO.'.
               
               
       END PROGRAM FLORICULTURA_ARQUIVO.
