from agents.workflow import ChaeUm

# from IPython.display import Image


try:
    with open(r"./image_all.png", "wb") as png:
        png.write(ChaeUm.get_graph(xray=1).draw_mermaid_png())
except Exception:
    pass
