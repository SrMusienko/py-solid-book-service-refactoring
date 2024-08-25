import json
import xml.etree.ElementTree as ET  # noqa: N817
from abc import ABC, abstractmethod


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, content: str, title: str) -> str:
        pass


class JsonSerializeStrategy(SerializeStrategy):
    def serialize(self, content: str, title: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializeStrategy(SerializeStrategy):
    def serialize(self, content: str, title: str) -> str:
        root = ET.Element("book")
        title_element = ET.SubElement(root, "title")
        title_element.text = title
        content_element = ET.SubElement(root, "content")
        content_element.text = content
        return ET.tostring(root, encoding="unicode")
