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
       01  CAMINHO-ARQUIVO PIC X(100) VALUE 'C:\Users\WIN 11\OneDrive' &
               '\Desktop\Floricultura' &
               '\Floricultura-4\scripts\tabela_plantas.txt'.

       01  STATUS-ARQUIVO.
           05 FS-ARQUIVO       PIC 9(02).
       
       01  WS-ARQUIVO          PIC X(80).

       77  QNT-PLANTAS         PIC 9(02) VALUE ZEROS.
        
       01  PLANTAS.
           03 LIDOS            PIC 9(02)
               OCCURS 1 TO 99 DEPENDING ON QNT-PLANTAS.
               
       77  I                   PIC 9(02) VALUE ZEROS.        
           
       01  TABELA-REGISTROS.
           03 REGISTROS        PIC X(90)
               OCCURS 1 TO 99 DEPENDING ON QNT-PLANTAS.
           
       01  WS-REGISTRO.
           05 WS-ID            PIC 9(02).
           05 WS-NOME          PIC X(30).
           05 WS-PRECO         PIC X(06).
           05 WS-PREFERENCIA   PIC X(41).

       01 WS-PRECO-NUM         PIC 9(08)V99.
       01 WS-PRECO-ED          PIC ZZZZZ9,99.

       01 REGISTRO-MOD.
           05 ID-MOD           PIC 9(02).
           05 FILLER           PIC X(01) VALUE '|'.
           05 NOME-MOD         PIC X(29).
           05 FILLER           PIC X(01) VALUE '|'.
           05 PRECO-MOD        PIC ZZZZZZ,ZZ.
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
                           PERFORM CONTA-REGISTRO                           
                           PERFORM MOVE-REGISTRO-PARA-TABELA
                           PERFORM MOSTRA-TABELA
                       END-IF
                   END-IF
           END-PERFORM.
           PERFORM QNT-REGISTRO-LIDO.    
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
          
          CONTA-REGISTRO.
              IF QNT-PLANTAS < 99
               COMPUTE QNT-PLANTAS = QNT-PLANTAS + 1
              END-IF. 
               
          QNT-REGISTRO-LIDO.
              DISPLAY 'FORAM LIDOS: ' QNT-PLANTAS ' REGISTROS'.
           
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
           
          MOVE-REGISTRO-PARA-TABELA.
              MOVE REGISTRO-MOD TO TABELA-REGISTROS.
              
          MOSTRA-TABELA.
              PERFORM VARYING I FROM 1 BY 1 UNTIL I > QNT-PLANTAS
                   DISPLAY REGISTROS(I)
              END-PERFORM.
           
          MOSTRA-ARQUIVO.
               DISPLAY '-----------------------------------------------'
      * ARQUIVO COM TAMANHO FIXO DE 80 CARACTERES
               DISPLAY  REGISTRO-MOD.
      *         DISPLAY 'ID: 'ID-MOD.
      *         DISPLAY 'NOME: 'NOME-MOD.
      *         DISPLAY 'PRECO: 'PRECO-MOD.
      *         DISPLAY 'PREFERENCIA: 'PREFERENCIA-MOD.

          FECHA-ARQUIVO.
               CLOSE ARQUIVO.
               IF FS-ARQUIVO NOT = 00
                 DISPLAY 'ERRO AO FECHAR O ARQUIVO. STATUS: ' FS-ARQUIVO
               ELSE
                DISPLAY '----------------------------------------------'
                DISPLAY 'ARQUIVO FECHADO COM SUCESSO.'.


       END PROGRAM FLORICULTURA_ARQUIVO.
