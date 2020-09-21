import argparse

def get_args():
    p = argparse.ArgumentParser(description="Hola Mundo",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('nombre', metavar='nombre', help='Digite su nombre')
    return p.parse_args()

def main():
    args = get_args()
    n = args.nombre
    print(f'Hola {n}')

if __name__ == '__main__':
    main()