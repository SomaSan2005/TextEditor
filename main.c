#include <stdio.h>
#include <string.h>
#include <ncurses.h>

#define MAX_ROWS 25
#define MAX_COLS 80
#define MAX_CHARS MAX_ROWS *MAX_COLS

char text[MAX_CHARS]; // Array per il testo
int row = 0, col = 0; // Variabili per tenere traccia della posizione corrente del cursore

// Funzione per visualizzare il testo sulla console
void display_text()
{
  clear(); // Pulisce la console
  for (int i = 0; i < MAX_ROWS; i++)
  {
    // Stampa il numero di riga
    mvprintw(i, 0, "%2d", i + 1);
    // Stampa il testo della riga
    for (int j = 0; j < MAX_COLS; j++)
    {
      mvaddch(i, j + 3, text[i * MAX_COLS + j]);
    }
  }
  // Evidenzia la posizione corrente del cursore
  move(row, col + 3);
  refresh(); // Aggiorna la console
}

int main()
{
  initscr();                    // Inizializza la libreria ncurses
  noecho();                     // Non visualizzare i caratteri inseriti dall'utente
  cbreak();                     // Non attendere il tasto invio per l'input
  keypad(stdscr, TRUE);         // Abilita i tasti freccia
  memset(text, ' ', MAX_CHARS); // Inizializza l'array di testo con spazi vuoti

  // Loop principale
  while (1)
  {
    display_text();   // Visualizza il testo sulla console
    int ch = getch(); // Legge un carattere dalla tastiera

    // Verifica se l'utente ha premuto un tasto freccia
    switch (ch)
    {
    case KEY_UP:
      if (row > 0)
        row--;
      break;
    case KEY_DOWN:
      if (row < MAX_ROWS - 1)
        row++;
      break;
    case KEY_LEFT:
      if (col > 0)
        col--;
      break;
    case KEY_RIGHT:
      if (col < MAX_COLS - 1)
        col++;
      break;
    case KEY_BACKSPACE: // Cancella il carattere sotto il cursore
      if (col > 0)
      {
        col--;
        text[row * MAX_COLS + col] = ' ';
      }
      break;
    default: // Inserisce il carattere sotto il cursore
      text[row * MAX_COLS + col] = (char)ch;
      if (col < MAX_COLS - 1)
        col++;
      break;
    }
  }

  endwin(); //
  endwin(); // Termina la sessione ncurses
  return 0;
}
