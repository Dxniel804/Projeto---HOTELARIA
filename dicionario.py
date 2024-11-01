import os

j = 1
cadastro = []
atendentes = []
admin_password = "admhotel123"
admin_email = "adm2406@gmail.com"

quartos_economicos = {
    1: {"descricao": "Um espaço básico com duas camas individuais, uma pequena área de estar e um banheiro compartilhado.\n", "status": "Disponivel\n"},
    2: {"descricao": "Um ambiente simples com duas camas de solteiro, uma mesa pequena e um banheiro compartilhado.\n", "status": "Disponivel\n"},
    3: {"descricao": "Um quarto modesto com duas camas simples, uma cadeira e um banheiro compartilhado.\n", "status": "Disponivel\n"},
    4: {"descricao": "Este quarto oferece duas camas individuais, uma pequena área de estar e um banheiro compartilhado.\n", "status": "Disponivel\n"},
    5: {"descricao": "Com duas camas simples, uma mesa dobrável e um banheiro compartilhado, este quarto oferece o essencial para uma estadia confortável a um preço acessível.\n", "status": "Disponivel\n"},
    6: {"descricao": "Um espaço despretensioso com duas camas individuais, uma cadeira e um banheiro compartilhado.\n", "status": "Disponivel\n"},
    7: {"descricao": "Equipado com duas camas simples, uma mesa pequena e um banheiro compartilhado, este quarto oferece uma estadia simples e confortável para viajantes conscientes do orçamento.\n", "status": "Disponivel\n"},
    8: {"descricao": "Um ambiente simples com duas camas individuais, uma poltrona e um banheiro compartilhado.\n", "status": "Disponivel\n"},
    9: {"descricao": "Este quarto dispõe de duas camas simples, uma pequena área de estar e um banheiro compartilhado.\n", "status": "Disponivel\n"},
    10: {"descricao": "Com duas camas individuais, uma mesa simples e um banheiro compartilhado, este quarto oferece uma opção confortável e acessível para todos os tipos de viajantes.\n", "status": "Disponivel\n"}
}

quartos_intermediarios = {
    11: {"descricao": "Um quarto acolhedor com uma cama de casal, uma área de estar confortável e um banheiro privativo. Ideal para casais ou viajantes que procuram um pouco mais de conforto.\n", "status": "Disponivel\n"},
    12: {"descricao": "Um ambiente confortável com uma cama de casal, uma mesa de trabalho e um banheiro privativo. Perfeito para estadias de negócios ou lazer.\n", "status": "Disponivel\n"},
    13: {"descricao": "Um quarto bem decorado com uma cama de casal, uma poltrona aconchegante e um banheiro privativo. Adequado para aqueles que buscam um espaço relaxante e funcional.\n", "status": "Disponivel\n"},
    14: {"descricao": "Este quarto oferece uma cama de casal, uma área de estar com sofá e um banheiro privativo. Uma escolha excelente para quem valoriza o espaço e o conforto.\n", "status": "Disponivel\n"},
    15: {"descricao": "Com uma cama de casal, uma mesa de trabalho espaçosa e um banheiro privativo, este quarto oferece o equilíbrio perfeito entre conforto e praticidade.\n", "status": "Disponivel\n"},
    16: {"descricao": "Um espaço elegante com uma cama de casal, uma poltrona confortável e um banheiro privativo. Perfeito para viajantes que desejam uma estadia confortável e agradável.\n", "status": "Disponivel\n"},
    17: {"descricao": "Equipado com uma cama de casal, uma pequena área de estar e um banheiro privativo, este quarto oferece uma estadia confortável e conveniente para todos os tipos de viajantes.\n", "status": "Disponivel\n"},
    18: {"descricao": "Um ambiente acolhedor com uma cama de casal, uma mesa de trabalho e um banheiro privativo. Ideal para estadias prolongadas ou para quem deseja um pouco mais de espaço.\n", "status": "Disponivel\n"},
    19: {"descricao": "Este quarto dispõe de uma cama de casal, uma área de estar com poltrona e um banheiro privativo. Ideal para viajantes que buscam conforto e funcionalidade.\n", "status": "Disponivel\n"},
    20: {"descricao": "Com uma cama de casal, uma mesa de trabalho e um banheiro privativo, este quarto oferece uma opção confortável e bem equipada para uma estadia agradável.\n", "status": "Disponivel\n"}
}

quartos_luxuosos = {
    21: {"descricao": "Um quarto espaçoso com cama king size, área de estar elegante e banheiro privativo com banheira. Perfeito para quem busca o máximo de conforto e sofisticação.\n", "status": "Disponivel\n"},
    22: {"descricao": "Ambiente refinado com cama king size, sala de estar separada e banheiro privativo com amenities de luxo. Ideal para uma estadia inesquecível.\n", "status": "Disponivel\n"},
    23: {"descricao": "Quarto elegante com cama king size, área de trabalho sofisticada e banheiro privativo com hidromassagem. Perfeito para relaxamento e produtividade.\n", "status": "Disponivel\n"},
    24: {"descricao": "Este quarto oferece cama king size, sala de estar ampla e banheiro privativo com banheira de hidromassagem. Uma escolha de luxo e conforto.\n", "status": "Disponivel\n"},
    25: {"descricao": "Com cama king size, área de estar luxuosa e banheiro privativo com amenidades premium, este quarto é perfeito para uma estadia luxuosa.\n", "status": "Disponivel\n"},
    26: {"descricao": "Um espaço requintado com cama king size, poltronas elegantes e banheiro privativo com banheira. Perfeito para uma experiência de luxo e conforto.\n", "status": "Disponivel\n"},
    27: {"descricao": "Equipado com cama king size, área de estar espaçosa e banheiro privativo com banheira de hidromassagem, este quarto oferece uma estadia luxuosa.\n", "status": "Disponivel\n"},
    28: {"descricao": "Ambiente sofisticado com cama king size, sala de estar e banheiro privativo com banheira de hidromassagem. Ideal para uma experiência inesquecível.\n", "status": "Disponivel\n"},
    29: {"descricao": "Este quarto dispõe de cama king size, área de estar elegante e banheiro privativo com amenities premium. Perfeito para uma estadia de luxo.\n", "status": "Disponivel\n"},
    30: {"descricao": "Com cama king size, sala de estar luxuosa e banheiro privativo com banheira, este quarto oferece uma opção de estadia sofisticada e confortável.\n", "status": "Disponivel\n"}
}

os.system('paus')