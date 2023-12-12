from PIL import Image, ImageFont, ImageDraw
import pandas

# Global Variables
font_nama = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 180)
font_warna = "#FFFFFF"

template = Image.open(r'template.png')
lebar, tinggi = template.size


def sertifikat(nama_siswa):
    '''Function to save certificates as a .png file'''

    sertifikat_template = Image.open(r'template.png')
    draw = ImageDraw.Draw(sertifikat_template)

    # Finding the width and height of the text.
    name_width, name_height = draw.textsize(nama_siswa, font=font_nama)

    # Placing it in the center, then making some adjustments.
    draw.text(((lebar - name_width) / 2, (tinggi - name_height) / 2 - 30), nama_siswa, fill=font_warna, font=font_nama)

    # Saving the certificates in a different directory.
    sertifikat_template.save("./serti/" + nama_siswa + ".png")
    # print('Menyimpan serfitikat:', nama_siswa)


if __name__ == "__main__":
    names_df = pandas.read_csv('names.csv', sep='#')
    for index, row in names_df.iterrows():
        name = row['Nama']  # Assuming 'Nama' is the column containing the names
        sertifikat(name)

    print(len(names_df), "certificates done.")
