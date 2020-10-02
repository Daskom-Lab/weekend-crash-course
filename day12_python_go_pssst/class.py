class Hewan:
    """
    Ini adalah hewan
    """

    def ngomong(self):
        print('ga bisa ngomong')

    def __init__(self):
        print('inisialisasi...')

if __name__ == "__main__":
    hewan = Hewan()
    hewan.ngomong()