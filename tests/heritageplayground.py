from rich.pretty import pprint
import heritage
import logging

import time


def main():
    # s = "हरे कृष्ण हरे कृष्ण कृष्ण कृष्ण हरे हरे हरे राम हरे राम राम राम हरे हरे"
    s = "हरे कृष्ण हरे राम"
    # s = "हरे"
    # s = "कृष्ण"
    # s = "राम"

    # puzzle:
    # verify for output:
    s = "आचार्य उपाध्याय कवि चक्र वर्तिन् ज्योति र्विद् ज्यौतिषक तर्क वाग् ईश दीक्षित दैव ज्ञ पण्डित भट्ट भट्टाचार्य वाजपेयिन् शर्मन् शास्त्रिन् संयमिन् सूरि"

    # compare to: https://sanskrit.inria.fr/cgi-bin/SKT/sktgraph2.cgi?lex=MW&st=t&us=f&font=roma&text=aacaarya+upaadhyaaya+kavi+cakra+vartin+jyoti+rvid+jyauti.saka+tarka+vaag+iiza+diik.sita+daiva+j%7Ena+pa.n.dita+bha.t.ta+bha.t.taacaarya+vaajapeyin+zarman+zaastrin+sa.myamin+suuri&t=VH&topic=&mode=f&corpmode=&corpdir=&sentno=

    # logging.basicConfig(level=logging.DEBUG)

    h = heritage.HeritagePlatform(
        base_url="http://localhost:4040/cgi-bin/",
        base_dir="/var/lib/heritage/sanskrit-heritage/Heritage_Platform",
    )

    first = time.time()
    # h.set_font("roma")
    # pprint(h.hydrate_sentence(h.get_analysis(s)))
    h.set_method("web")
    h.set_font("roma")
    print(f"{first}: step connect")
    print(h)
    analysis = h.get_analysis(s)
    second = time.time()
    pprint(analysis)
    print(f"{second}: step load segment OK ({second - first}s incr)")
    hydrated = h.hydrate_sentence(analysis)  # slowww
    third = time.time()
    # hydrated = analysis
    print(f"{third}: step hydrate sentence OK ({third - second}s incr)")
    for k, v in hydrated.items():
        pprint(
            dict(
                search=s,
                solution=v["words"],
            )
        )
    four = time.time()
    print(f"{four}: all done ({four-first}s total)")
    #     for word in v["words"]:
    # words = hydrated["0"]["words"]
    # for term in words:
    #     for variant in term:
    #         pprint(variant)


if __name__ == "__main__":
    main()
