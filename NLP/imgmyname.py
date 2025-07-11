from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
name="Likhitha "
text=(name+'') * 100
mask=np.array(Image.open("heart_img (1).webp"))
wordcloud=WordCloud(background_color="white",mask=mask,
                    contour_color="red",contour_width=0.5
                    ,colormap="brg").generate(text)
plt.figure(figsize=(8,8))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()