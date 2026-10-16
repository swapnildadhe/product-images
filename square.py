import sys,glob
from PIL import Image
for f in glob.glob(sys.argv[1]+'/*.jpg'):
    im=Image.open(f).convert('RGB')
    if f.split('/')[-1].startswith('ingredients'):
        w,h=im.size; im=im.crop((8,8,w-8,h-8))
    w,h=im.size; s=int(max(w,h)*1.06)
    c=Image.new('RGB',(s,s),(255,255,255)); c.paste(im,((s-w)//2,(s-h)//2))
    c.save(f,quality=95); print(f,c.size)
