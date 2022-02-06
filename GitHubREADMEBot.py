import os
import re
from PIL import Image


class GitHubREADMEBot:

    PATHS = {
        "kakao": "",
        # "kubernetes": "",
        # "": ""
    }

    def __init__(self, keyword, image_path="kakao"):
        self.keyword = keyword
        if image_path == 'kakao':
            self.image_path = self.PATHS[image_path]
        else:
            self.image_path = image_path


    def rename_image(self):
        image_dir = os.listdir(self.image_path)

        for i, image_file in enumerate(image_dir):
            old_name = f"{self.image_path}\\{image_file}"
            if (i < 9):
                new_name = f"{self.image_path}\\{self.keyword} 0{i+1}.png"
            else:
                new_name = f"{self.image_path}\\{self.keyword} {i+1}.png"

            os.rename(old_name, new_name)


    def crop_image(self, coordinates):
        image_dir = os.listdir(self.image_path)

        coor_dict = {"aws": (740, 275, 2030, 1000),
                "phone": (150, 0, 2070, 1080),}

        if type(coordinates) == str:
            crop_size = coor_dict[coordinates]
        else:
            crop_size = coordinates

        for image_file in image_dir:
            path = f"{self.image_path}\\{image_file}"
            img = Image.open(path)
            #   = img.crop((w_s, h_s, w_e, h_e))
            img = img.crop(crop_size)
            img.save(f"{self.image_path}/{image_file}")


    def generate_image_script(self, url, width):
        # folder location
        image_dir = os.listdir(self.image_path)
        image_dir.sort()
        github_url = re.sub('tree', 'blob', url)

        for image_file in image_dir:
            path = f"{github_url}/{image_file}"
            path = re.sub(" ", "%20", path)
            img_tag = f'<img src="{path}" width={width} />'
            print(img_tag)


    def create_table(self, num_row, num_column):

        if (num_row < 1 or num_column < 1):
            print('Row/column cannot be less than 1.')

        column    = "    |"
        separator = " -- |"

        row       = "|"
        sep_row   = "|"
        for _ in range(num_column):
            row     += column
            sep_row += separator

        for i in range(num_row + 1):
            if (i == 1): print(sep_row)
            else: print(row)


    def generate_references(self):

        print("### References\n")
        print("  - ")


if __name__ == "__main__":

#    url = "https://github.com/Coding-Forest/2022-AWS-Certificaiton/tree/main/0%20AWS%20Training/Elastic%20Beanstalk"
#    image_path = ""
    url = "https://github.com/deep-woods/2022-Docker/tree/main/images"
    gb = GitHubREADMEBot("Linux", "")

#    gb.create_table(7, 7)
#    gb.rename_image()
#    gb.crop_image("phone")
    gb.generate_image_script(url=url, width=1000)
#    gb.generate_references()
