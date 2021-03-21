blocks=int(input("Wprowadź liczbę bloków: "))

layer=0
in_layer=1
while blocks >= in_layer:
    layer = layer + 1
    blocks = blocks - in_layer
    in_layer += 1
    print("Warstwa: ", layer, "- Pozostało", blocks, "klocków")
    