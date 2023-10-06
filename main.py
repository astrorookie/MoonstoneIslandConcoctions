from functions import *
import streamlit as st
import pandas as pd



df = pd.read_csv('allconcocs.csv')
dict = df.to_dict('records')

st.header("astro's concoction helper for moonstone island")

st.header('Concoction Predictor')

cola, colb = st.columns(2)

with cola:
    st.subheader('First Plant')
    firstplant = st.selectbox('Select first plant', allplantslist2)
    firstfert = st.selectbox('Select first fertiliser',fertlist)



with colb:
    st.subheader('Second Plant')
    secondplant = st.selectbox('Select second plant', allplantslist2)
    secondfert = st.selectbox('Select second fertiliser',fertlist)

a = getplantfromlist(firstplant)
b = getplantfromlist(secondplant)

A = getfertfromlist(firstfert,a)
B = getfertfromlist(secondfert,b)


st.subheader('End concoction will have:')

concoction = concoc(A,B)
col1, col2 = st.columns(2)

with col1:
    st.write('Stamina: ' + str(concoction['Stamina']))
    st.write('EXP: ' + str(concoction['Exp']))
    st.write('HP: ' + str(concoction['HP']))
    st.write('Tame: ' + str(concoction['Tame']))

with col2:
    st.write('Vitality: ' + str(concoction['Vitality']))
    st.write('Armour: ' + str(concoction['Armour']))
    st.write('Speed: ' + str(concoction['Speed']))
    st.write('Power: ' + str(concoction['Power']))

st.write('-------')

st.header('Concoction Calculator')
st.write('Insert a number or "ANY" if that stat does not matter!')
col3, col4 = st.columns(2)

with col3:
    stamsearch1 = st.text_input('Stamina')
    expsearch1 = st.text_input('EXP')
    hpsearch1 = st.text_input('HP')
    tamesearch1 = st.text_input('Tame')
with col4:
    vitalsearch1 = st.text_input('Vitality')
    speedsearch1 = st.text_input('Speed')
    armoursearch1 = st.text_input('Armour')
    powersearch1 = st.text_input('Power')


possiblecombos = []

if st.button("Calculate Ingredients"):
    st.header('Combinations:')
    if stamsearch1 != 'ANY':
        stamsearch = int(stamsearch1)
    else:
        stamsearch = 'ANY'

    if expsearch1 != 'ANY':
        expsearch = int(expsearch1)
    else:
        expsearch = 'ANY'

    if hpsearch1 != 'ANY':
       hpsearch = int(hpsearch1)
    else:
        hpsearch = 'ANY'

    if tamesearch1 != 'ANY':
        tamesearch = int(tamesearch1)
    else:
        tamesearch = 'ANY'

    if vitalsearch1 != 'ANY':
        vitalsearch = int(vitalsearch1)
    else:
        vitalsearch = 'ANY'

    if speedsearch1 != 'ANY':
        speedsearch = int(speedsearch1)
    else:
        speedsearch = 'ANY'

    if armoursearch1 != 'ANY':
        armoursearch = int(armoursearch1)
    else:
        armoursearch = 'ANY'

    if powersearch1 != 'ANY':
        powersearch = int(powersearch1)
    else:
        powersearch = 'ANY'

    for concoc in dict:
        name = concoc['Name1']
        stam = concoc['Stamina']
        exp = concoc['Exp']
        hp = concoc['HP']
        tame = concoc['Tame']
        vital = concoc['Vitality']
        armour = concoc['Armour']
        speed = concoc['Speed']
        power = concoc['Power']

        thisconcoc = searchf(stam,stamsearch,concoc)

        if thisconcoc != 'No':
            thisconcoc = searchf(exp,expsearch,concoc)

            if thisconcoc != 'No':
                thisconcoc = searchf(hp, hpsearch, concoc)

                if thisconcoc != 'No':
                    thisconcoc = searchf(tame, tamesearch, concoc)

                    if thisconcoc != 'No':
                        thisconcoc = searchf(vital, vitalsearch, concoc)

                        if thisconcoc != 'No':
                            thisconcoc = searchf(armour, armoursearch, concoc)

                            if thisconcoc != 'No':
                                thisconcoc = searchf(speed, speedsearch, concoc)

                                if thisconcoc != 'No':
                                    thisconcoc = searchf(power, powersearch, concoc)

                                    if thisconcoc != 'No':

                                        st.subheader(concoc['Name1'])
                                        st.write(concoc)
                                    else:
                                        x=7

                                else:
                                    x=6

                            else:
                                x=5

                        else:
                            x=4

                    else:
                        x=3

                else:
                    x=2


            else:
                x=2

        else:
            x = 2




else:
    thisconcoc = 'no concoc :('
    st.write(thisconcoc)




