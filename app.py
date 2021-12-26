from random import randrange
import streamlit as st
from PIL import Image
import base64
import py_avataaars as pa


st.markdown("""
# AVATAR MAKER
Build your own avatars or generate random avatars!!

**Credits**
- App built using `Python` and `Streamlit` by Tushara 
- App inspired by the [avataaars generator](https://getavataaars.com) by [Fang-Pen Lin](https://twitter.com/fangpenlin)
- Built with [py_avataaars](https://pypi.org/project/py-avataaars/) library by [Krzysztof Ebert](https://github.com/kebu)
- Avatar is based on Sketch library [Avataaars](https://avataaars.com) designed by [Pablo Stanley](https://twitter.com/pablostanley).
---
""")

st.sidebar.header('Choose your avatar features')

options = st.sidebar.selectbox('Style' , ('CIRCLE' , 'TRANSPARENT'))


tops = ['NO_HAIR','EYE_PATCH','HAT','HIJAB','TURBAN',
                 'WINTER_HAT1','WINTER_HAT2','WINTER_HAT3',
                 'WINTER_HAT4','LONG_HAIR_BIG_HAIR','LONG_HAIR_BOB',
                 'LONG_HAIR_BUN','LONG_HAIR_CURLY','LONG_HAIR_CURVY',
                 'LONG_HAIR_DREADS','LONG_HAIR_FRIDA','LONG_HAIR_FRO',
                 'LONG_HAIR_FRO_BAND','LONG_HAIR_NOT_TOO_LONG',
                 'LONG_HAIR_SHAVED_SIDES','LONG_HAIR_MIA_WALLACE',
                 'LONG_HAIR_STRAIGHT','LONG_HAIR_STRAIGHT2',
                 'LONG_HAIR_STRAIGHT_STRAND','SHORT_HAIR_DREADS_01',
                 'SHORT_HAIR_DREADS_02','SHORT_HAIR_FRIZZLE',
                 'SHORT_HAIR_SHAGGY_MULLET','SHORT_HAIR_SHORT_CURLY',
                 'SHORT_HAIR_SHORT_FLAT','SHORT_HAIR_SHORT_ROUND',
                 'SHORT_HAIR_SHORT_WAVED','SHORT_HAIR_SIDES',
                 'SHORT_HAIR_THE_CAESAR','SHORT_HAIR_THE_CAESAR_SIDE_PART']

hat_colors = ['BLACK', 'PASTEL_YELLOW','PINK','RED','WHITE', 'PASTEL_GREEN',
        'PASTEL_ORANGE', 'PASTEL_BLUE' , 'PASTEL_RED', 'BLUE_01', 'BLUE_02',
        'BLUE_03', 'GRAY_01' , 'GRAY_02' , 'HEATHER' ]
skin_colors = ['TANNED','YELLOW','PALE','LIGHT','BROWN','DARK_BROWN','BLACK']
hair_colors = ['BLACK','BLONDE','BROWN','BLONDE_GOLDEN', 'BROWN_DARK' , 'PLATINUM', 'RED', 'SILVER_GRAY', 'AUBURN' , 'PASTEL_PINK' , 'PASTEL_BLUE', 'PASTEL_GREEN']

facial_hair_type = ['DEFAULT','BEARD_MEDIUM','BEARD_LIGHT','BEARD_MAJESTIC','MOUSTACHE_FANCY','MOUSTACHE_MAGNUM']
facial_hair_color = ['AUBURN','BLACK','BLONDE','BLONDE_GOLDEN','BROWN','BROWN_DARK','PLATINUM','RED']
mouth_type = ['DEFAULT','CONCERNED','DISBELIEF','EATING','GRIMACE','SAD','SCREAM_OPEN','SERIOUS','SMILE','TONGUE','TWINKLE','VOMIT']
eye_type = ['DEFAULT','CLOSE','CRY','DIZZY','EYE_ROLL','HAPPY','HEARTS','SIDE','SQUINT','SURPRISED','WINK','WINK_WACKY']
eyebrow_type = ['DEFAULT','DEFAULT_NATURAL','ANGRY','ANGRY_NATURAL','FLAT_NATURAL','RAISED_EXCITED','RAISED_EXCITED_NATURAL','SAD_CONCERNED','SAD_CONCERNED_NATURAL','UNI_BROW_NATURAL','UP_DOWN','UP_DOWN_NATURAL','FROWN_NATURAL']
accessories = ['DEFAULT','KURT','PRESCRIPTION_01','PRESCRIPTION_02','ROUND','SUNGLASSES','WAYFARERS']
clothes = ['BLAZER_SHIRT','BLAZER_SWEATER','COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK']
clothes_color = ['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']
clothe_graphic_type = ['BAT','CUMBIA','DEER','DIAMOND','HOLA','PIZZA','RESIST','SELENA','BEAR','SKULL_OUTLINE','SKULL']



if st.button('RANDOM AVATAR'):
    index_skin_color = randrange(0, len(skin_colors))
    index_top_type = randrange(0, len(tops))
    index_hair_color = randrange(0, len(hair_colors))
    index_hat_color = randrange(0, len(hat_colors))
    index_facial_hair_type = randrange(0, len(facial_hair_type))
    index_facial_hair_color= randrange(0, len(facial_hair_color))
    index_mouth_type = randrange(0, len(mouth_type))
    index_eye_type = randrange(0, len(eye_type))
    index_eyebrow_type = randrange(0, len(eyebrow_type))
    index_accessories_type = randrange(0, len(accessories))
    index_clothe_type = randrange(0, len(clothes))
    index_clothe_color = randrange(0, len(clothes_color))
    index_clothe_graphic_type = randrange(0, len(clothe_graphic_type))

else:
    index_skin_color = 0
    index_top_type = 0
    index_hair_color = 0
    index_hat_color = 0
    index_facial_hair_type = 0
    index_facial_hair_color = 0
    index_mouth_type = 0
    index_eye_type = 0
    index_eyebrow_type = 0
    index_accessories_type = 0
    index_clothe_type = 0
    index_clothe_color = 0
    index_clothe_graphic_type = 0

select_skin_color = st.sidebar.selectbox('Skin color', skin_colors, index = index_skin_color)

st.sidebar.subheader('Customize Head')

select_top_type = st.sidebar.selectbox('Head top',
                                        tops,
                                        index = index_top_type)
select_hair_color = st.sidebar.selectbox('Hair color',
                                         hair_colors,
                                         index = index_hair_color)
select_hat_color = st.sidebar.selectbox('Hat color',
                                         hat_colors,
                                         index = index_hat_color)

st.sidebar.subheader('Customize Face')

select_facial_hair_type = st.sidebar.selectbox('Facial hair type',
                                                facial_hair_type,
                                                index = index_facial_hair_type)
select_facial_hair_color = st.sidebar.selectbox('Facial hair color',
                                                facial_hair_color,
                                                index = index_facial_hair_color)

select_eye_type = st.sidebar.selectbox('Eye type',
                                        eye_type,
                                        index = index_eye_type)
select_eyebrow_type = st.sidebar.selectbox('Eyebrow type',
                                            eyebrow_type,
                                            index = index_eyebrow_type)

select_mouth_type = st.sidebar.selectbox('Mouth type',
                                          mouth_type,
                                          index = index_mouth_type)

st.sidebar.subheader('Customize Clothes and Accessories')

select_accessories_type = st.sidebar.selectbox('Accessories type',
                                                accessories,
                                                index = index_accessories_type)
select_clothe_type = st.sidebar.selectbox('Clothe type',
                                           clothes,
                                           index = index_clothe_type)
select_clothe_color = st.sidebar.selectbox('Clothe Color',
                                            clothes_color,
                                            index = index_clothe_color)
select_clothe_graphic_type = st.sidebar.selectbox('Clothe graphic type',
                                                   clothe_graphic_type,
                                                   index = index_clothe_graphic_type)


avatar = pa.PyAvataaar(
    style = eval('pa.AvatarStyle.%s' % options),
    skin_color = eval('pa.SkinColor.%s' % select_skin_color),
    top_type = eval('pa.TopType.SHORT_HAIR_SHORT_FLAT.%s' % select_top_type),
    hair_color = eval('pa.HairColor.%s' % select_hair_color),
    hat_color = eval('pa.ClotheColor.%s' % select_hat_color),
    facial_hair_type = eval('pa.FacialHairType.%s' % select_facial_hair_type),
    facial_hair_color = eval('pa.FacialHairColor.%s' % select_facial_hair_color),
    mouth_type = eval('pa.MouthType.%s' % select_mouth_type),
    eye_type = eval('pa.EyesType.%s' % select_eye_type),
    eyebrow_type = eval('pa.EyebrowType.%s' % select_eyebrow_type),
    nose_type = pa.NoseType.DEFAULT,
    accessories_type = eval('pa.AccessoriesType.%s' % select_accessories_type),
    clothe_type = eval('pa.ClotheType.%s' % select_clothe_type),
    clothe_color = eval('pa.ClotheColor.%s' % select_clothe_color),
    clothe_graphic_type = eval('pa.ClotheGraphicType.%s' %select_clothe_graphic_type)
)


def downloadImage(filename):
    image_file = open(filename, 'rb')
    b64 = base64.b64encode(image_file.read()).decode()  
    href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download {filename} File</a>'
    return href

st.subheader('**My Avatar**')
rendered_avatar = avatar.render_png_file('myAvatar.png')
image = Image.open('myAvatar.png')
st.image(image)
st.markdown(downloadImage('myAvatar.png'), unsafe_allow_html=True)
