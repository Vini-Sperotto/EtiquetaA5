import fitz
import os


# ==========================
# CONFIGURAÇÕES
# ==========================

# Área da etiqueta no PDF original (em mm)
CROP_X = 2
CROP_Y = 2
CROP_W = 105
CROP_H = 148

# Margem superior na metade superior da folha A4 (em mm)
TOP_MARGIN = 10

# ==========================


def mm_to_pt(mm):
    return mm * 2.83465


def process_pdf(input_path, mode="save"):

    doc = fitz.open(input_path)

    page = doc[0]

    # Área da etiqueta
    clip = fitz.Rect(
        mm_to_pt(CROP_X),
        mm_to_pt(CROP_Y),
        mm_to_pt(CROP_X + CROP_W),
        mm_to_pt(CROP_Y + CROP_H)
    )

    # Cria novo PDF
    new_doc = fitz.open()

    # Tamanho A4
    a4_w = mm_to_pt(210)
    a4_h = mm_to_pt(297)

    page_new = new_doc.new_page(
        width=a4_w,
        height=a4_h
    )

    # Após girar 90°
    rot_w = mm_to_pt(CROP_H)   # 148 mm
    rot_h = mm_to_pt(CROP_W)   # 105 mm

    # Centraliza horizontalmente
    cx = (a4_w - rot_w) / 2

    # Metade superior da folha
    half_h = a4_h / 2

    # Centraliza na metade superior
    cy = (half_h - rot_h) / 2

    # Acrescenta margem superior
    cy += mm_to_pt(TOP_MARGIN)

    page_new.show_pdf_page(
        fitz.Rect(
            cx,
            cy,
            cx + rot_w,
            cy + rot_h
        ),
        doc,
        0,
        clip=clip,
        rotate=90
    )

    # Copia as demais páginas sem alteração
    if len(doc) > 1:
        new_doc.insert_pdf(
            doc,
            from_page=1,
            to_page=len(doc) - 1
        )

    base = os.path.basename(input_path)

    output_path = os.path.join(
        os.path.dirname(input_path),
        f"A5_{base}"
    )

    new_doc.save(output_path)

    new_doc.close()
    doc.close()

    return output_path