import argparse

def get_args():
    f = argparse.ArgumentParser(description="Hola Mundo",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    f.add_argument('nombre', metavar='nombre', help='Digite su nombre')
    return f.parse_args()

def main():
    args = get_args()
    n = args.nombre
    print(f'Hola {n}')

if __name__ == '__main__':
    main()