import qrcode

def generate_qr(data, file_name='qrcode.png', size=10, border=4):
    """
    Génère un QR code avec les paramètres donnés.
    
    :param data: Texte ou URL à encoder dans le QR code
    :param file_name: Nom du fichier de sortie (avec extension .png par défaut)
    :param size: Taille des blocs du QR code
    :param border: Taille de la bordure en blocs
    """
    qr = qrcode.QRCode(
        version=1,  # version 1 = plus petite taille possible, ajustée dynamiquement
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_name)
    print(f"QR code généré et enregistré sous {file_name}")

if __name__ == "__main__":
    texte = input("Entrez le texte ou l'URL à encoder : ")
    generate_qr(texte, "mon_qrcode.png")
