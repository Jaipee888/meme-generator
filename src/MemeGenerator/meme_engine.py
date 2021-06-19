from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    def __init__(self, output_dir):
        self.output_dir = output_dir + ".png"
        self.img_path = None
        self.text = None
        self.author = None
        self.width = None

    def make_meme(self, img_path, text, author, width=500) -> str:
        self.img_path = img_path
        self.text = text
        self.author = author
        self.width = width

        self.img = Image.open(self.img_path)

        if self.width is not None:
            ratio = self.width / float(self.img.size[0])
            height = int(ratio * float(self.img.size[1]))
            self.img = self.img.resize((self.width, height), Image.NEAREST)

        fnt = ImageFont.truetype("./open-sans/OpenSans-Bold.ttf", 20)
        draw = ImageDraw.Draw(self.img)
        body = self.text + ", -- " + self.author
        draw.multiline_text((10, 10), body, font=fnt)
        self.img.save(self.output_dir)

        return self.output_dir
