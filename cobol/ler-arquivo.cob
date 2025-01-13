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
           'C:\Users\WIN 11\Floricultura\Floricultura-2' &
               '\scripts\tabela_plantas.txt'.

       01  STATUS-ARQUIVO.
           05 FS-ARQUIVO       PIC 9(02).

       01  WS-ARQUIVO          PIC X(80).

       01  WS-REGISTRO.
           05 WS-ID            PIC 9(01).
           05 WS-NOME          PIC X(30).
           05 WS-PRECO         PIC 9(8)V99.
           05 WS-PREFERENCIA   PIC X(41).

       01 WS-PRECO-ED          PIC ZZZZZZZZ,ZZ.

       01 EOF                  PIC X(01) VALUE 'N'.
       01 CABECALHO            PIC X(01) VALUE 'N'.

      *
         PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM ABRE-ARQUIVO.
      *    RETIRAR OS DOIS CABEÇALHOS
           PERFORM LE-ARQUIVO 2 TIMES.
           MOVE 'Y' TO CABECALHO.
           PERFORM UNTIL EOF = 'Y'
                   PERFORM LE-ARQUIVO
                   IF EOF NOT = 'Y'
                       IF CABECALHO = 'Y'
                           PERFORM UNSTRING-ARQUIVO
                           PERFORM MOSTRA-ARQUIVO
                       END-IF
                   END-IF
           END-PERFORM.
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
                   READ ARQUIVO INTO WS-ARQUIVO
                   AT END
                       MOVE 'Y' TO EOF.

          UNSTRING-ARQUIVO.
               UNSTRING WS-ARQUIVO
                   DELIMITED BY ';'
                   INTO WS-ID
                        WS-NOME
                        WS-PRECO
                        WS-PREFERENCIA
              END-UNSTRING.

          EDITA-PRECO.
              MOVE WS-PRECO TO WS-PRECO-ED.

          MOSTRA-ARQUIVO.
               DISPLAY '-------------------------------------------'
      * ARQUIVO COM TAMANHO FIXO DE 80 CARACTERES
               DISPLAY  WS-REGISTRO.
               DISPLAY 'ID: 'WS-ID.
               DISPLAY 'NOME: 'WS-NOME.
               DISPLAY 'PRECO: 'WS-PRECO-ED.
               DISPLAY 'PREFERENCIA: 'WS-PREFERENCIA.

          FECHA-ARQUIVO.
               CLOSE ARQUIVO.
               IF FS-ARQUIVO NOT = 00
                 DISPLAY 'ERRO AO FECHAR O ARQUIVO. STATUS: ' FS-ARQUIVO
               ELSE
                 DISPLAY 'ARQUIVO FECHADO COM SUCESSO.'.


       END PROGRAM FLORICULTURA_ARQUIVO.
