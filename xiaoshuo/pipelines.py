# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class XiaoshuoPipeline:
    a = 0

    def open_spider(self, spider):
        print("start")
        self.file = open("武道宗师.txt", "w")

    def close_spider(self, spider):
        print("end")
        self.file.close()

    def process_item(self, item, spider):
        self.a += 1
        print(self.a)
        item["title"] = str(item["title"]).strip()
        item["content"] = [str(i) for i in item["content"]]
        item["content"] = "\n    ".join("".join(item["content"]).split())
        s = item["title"] + "\n    " + item["content"] + "\n\n"
        self.file.write(s)
        return item
