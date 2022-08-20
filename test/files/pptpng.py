import aspose.slides as slides
import aspose.pydrawing as drawing

# Load presentation
pres = slides.Presentation("Decisionmaking.pptx")

# Loop through slides
for index in range(pres.slides.length):
    # Get reference of slide
    slide = pres.slides[index]

    # Save as PNG
    slide.get_thumbnail().save("slide_{i}.png".format(i = index), drawing.imaging.ImageFormat.png)