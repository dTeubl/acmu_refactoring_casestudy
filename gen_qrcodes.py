#!/usr/bin/python
import qrcode as qr

link = "https://gitlab.lrz.de/lls/acmu/acmu-software"
acmu_repo = qr.make(link)
acmu_repo.save("./figs/qr_acmu_repo.png")

link = "https://github.com/dTeubl/acmu_refactoring_casestudy"
slides = qr.make(link)
slides.save("./figs/qr_slides.png")

link = "https://htmlpreview.github.io/?https://github.com/dTeubl/acmu_refactoring_casestudy/blob/main/refactoring.html#"
slides = qr.make(link)
slides.save("./figs/preview.png")
