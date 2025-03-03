from rich.pretty import pprint
import heritage
import logging


def main():
    # s = "हरे कृष्ण हरे कृष्ण कृष्ण कृष्ण हरे हरे हरे राम हरे राम राम राम हरे हरे"
    s = "हरे कृष्ण"
    # logging.basicConfig(level=logging.DEBUG)
    h = heritage.HeritagePlatform(
        base_url="http://localhost:4040/cgi-bin/",
        base_dir="/var/lib/heritage/sanskrit-heritage/Heritage_Platform",
    )
    # h.set_font("roma")
    pprint(h.hydrate_sentence(h.get_analysis(s)))
    h.set_method("web")
    # h.set_font("roma")
    pprint(h.hydrate_sentence(h.get_analysis(s)))


if __name__ == "__main__":
    main()
