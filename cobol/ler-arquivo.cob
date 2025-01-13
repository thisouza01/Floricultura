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
           05 WS-PRECO         PIC X(08).
           05 WS-PREFERENCIA   PIC X(41).

       01 WS-PRECO-NUM         PIC 9(08)V99.    
       01 WS-PRECO-ED          PIC ZZZZZZZ9,99.
       
       01 REGISTRO-MOD.
           05 ID-MOD           PIC 9(01).
           05 FILLER           PIC X(01) VALUE '|'.
           05 NOME-MOD         PIC X(29).
           05 FILLER           PIC X(01) VALUE '|'.
           05 PRECO-MOD        PIC ZZZZZZZZ,ZZ.
           05 FILLER           PIC X(01) VALUE '|'.
           05 PREFERENCIA-MOD  PIC X(40).           
           
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
                           PERFORM CONVERTE-NUM
                           PERFORM EDITA-PRECO
                           PERFORM MOVE-REGISTRO
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

          CONVERTE-NUM.
              INSPECT WS-PRECO CONVERTING '.' TO ','.
              MOVE FUNCTION NUMVAL-C(WS-PRECO) TO WS-PRECO-NUM.
              
              
          EDITA-PRECO.
              MOVE WS-PRECO-NUM TO WS-PRECO-ED.
              
          MOVE-REGISTRO.
              MOVE WS-ID TO ID-MOD.
              MOVE WS-NOME TO NOME-MOD.
              MOVE WS-PRECO-NUM TO PRECO-MOD.
              MOVE WS-PREFERENCIA TO PREFERENCIA-MOD.

          MOSTRA-ARQUIVO.
               DISPLAY '-------------------------------------------'
      * ARQUIVO COM TAMANHO FIXO DE 80 CARACTERES
               DISPLAY  REGISTRO-MOD.
               DISPLAY 'ID: 'ID-MOD.
               DISPLAY 'NOME: 'NOME-MOD.
               DISPLAY 'PRECO: 'PRECO-MOD.
               DISPLAY 'PREFERENCIA: 'PREFERENCIA-MOD.

          FECHA-ARQUIVO.
               CLOSE ARQUIVO.
               IF FS-ARQUIVO NOT = 00
                 DISPLAY 'ERRO AO FECHAR O ARQUIVO. STATUS: ' FS-ARQUIVO
               ELSE
                 DISPLAY '-------------------------------------------'                   
                 DISPLAY 'ARQUIVO FECHADO COM SUCESSO.'.


       END PROGRAM FLORICULTURA_ARQUIVO.
