from apps.galeria.models import Photograph

photograph1 = Photograph(name="Nebulosa de Carina",
                         legend="webbtelescope.org / NASA / James Webb",
                         file_name="carina-nebula.png")
photograph1.save()

photograph2 = Photograph(name="Galáxia NGC 1079",
                         legend="nasa.org / NASA / Hubble",
                         file_name="hubble_ngc1079.png")
photograph2.save()