import ahorcado
import tateti


def main(args):
	
	sigo_jugando = True
	while sigo_jugando:
		
		print('''
		Elegí con qué juego querés jugar:
		1.- Ahorcado
		2.- Ta-TE-TI
		4.- Salir''')

		opcion = input()
		if opcion == '1':
			hangman.main()
		elif opcion == '2':
			tictactoeModificado.main()
		elif opcion == '4':
			sigo_jugando = False
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))