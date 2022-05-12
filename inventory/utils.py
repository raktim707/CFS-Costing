
def getDimension(material):
    active_fields = []
    if material.width1:
        active_fields.append('width1')
    if material.width2:
        active_fields.append('width2')
    if material.height:
        active_fields.append('height')
    if material.diameter1:
        active_fields.append('diameter1')
    if material.diameter2:
        active_fields.append('diameter2')
    if material.weight:
        active_fields.append('weight')
    if material.volume:
        active_fields.append("volume")
    return active_fields


def getMatDim(material, m):
    active_fields = []
    if material.width1:
        active_fields.append(['width1', m.width1])
    if material.width2:
        active_fields.append(['width2', m.width2])
    if material.height:
        active_fields.append(['height', m.height])
    if material.diameter1:
        active_fields.append(['diameter1', m.diameter1])
    if material.diameter2:
        active_fields.append(['diameter2', m.diameter2])
    if material.weight:
        active_fields.append(['weight', m.weight])
    if material.volume:
        active_fields.append(["volume", m.volume])
    return active_fields
