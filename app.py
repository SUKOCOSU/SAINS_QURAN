import json
import streamlit as st

st.set_page_config(
    page_title="Ensiklopedia Ayat Sains Al-Qur'an",
    page_icon="🌌",
    layout="wide",
)

st.markdown(
    "<h1 style='text-align: center; color: #1E3A8A;'>🌌 Ensiklopedia Ayat Sains Al-Qur'an</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center;'>Katalog & Analisis Interaktif Ayat-Ayat Kauniyah dalam Perspektif Sains Modern</p>",
    unsafe_allow_html=True,
)


@st.cache_data
def load_data():
    return [
        {
            "jilid": "Jilid 1: Kosmologi & Astrofisika",
            "surah": "Al-Anbiya' (21:30)",
            "arab": "أَوَلَمْ يَرَ الَّذِينَ كَفَرُوا أَنَّ السَّمَاوَاتِ وَالْأَرْضَ كَانَتَا رَتْقًا فَفَتَقْنَاهُمَا",
            "terjemahan": "Dan apakah orang-orang kafir tidak mengetahui bahwa langit dan bumi itu dulunya adalah suatu yang padu (ratqan), kemudian Kami pisahkan antara keduanya...",
            "sains": "Menerangkan konsep Singularitas Kosmik awal dan peristiwa Big Bang.",
            "tags": ["Big Bang", "Singularitas", "Astrofisika"],
        },
        {
            "jilid": "Jilid 1: Kosmologi & Astrofisika",
            "surah": "At-Tariq (86:1-3)",
            "arab": "وَالسَّمَاءِ وَالطَّارِقِ ﴿١﴾ وَمَا أ أَدْرَاكَ مَا الطَّارِقُ ﴿٢﴾ النَّجْمُ الثَّاقِبُ ﴿٣﴾",
            "terjemahan": "Demi langit dan At-Tariq... (yaitu) bintang yang mengetuk dan menembus.",
            "sains": "Mendeskripsikan Bintang Pulsar (bintang neutron berotasi tinggi) yang memancarkan ketukan pulsa teratur.",
            "tags": ["Pulsar", "Bintang Neutron", "Benda Langit"],
        },
        {
            "jilid": "Jilid 2: Geofisika & Meteorologi",
            "surah": "An-Naml (27:88)",
            "arab": "وَتَرَى الْجِبَالَ تَحْسَبُهَا جَامِدَةً وَهِيَ تَمُرُّ مَرَّ السَّحَابِ",
            "terjemahan": "Dan engkau melihat gunung-gunung itu, engkau sangka dia tetap di tempatnya, padahal ia berjalan sebagai jalannya awan...",
            "sains": "Menjelaskan fenomena rotasi Bumi dan pergeseran lempeng tektonik (Continental Drift).",
            "tags": ["Rotasi Bumi", "Tektonik", "Geologi"],
        },
        {
            "jilid": "Jilid 3: Biologi & Embriologi",
            "surah": "Al-Mu'minun (23:12-14)",
            "arab": "ثُمَّ خَلَقْنَا النُّطْفَةَ عَلَقَةً فَخَلَقْنَا الْعَلَقَةَ مُضْغَةً...",
            "terjemahan": "Kemudian Nutfah itu Kami jadikan 'Alaqah, lalu 'Alaqah Kami jadikan Mudghah...",
            "sains": "Menjelaskan tahapan spesifik perkembangan embrio manusia (Zigot, Implantasi, Somitogenesis).",
            "tags": ["Embriologi", "Anatomi", "Biologi"],
        },
    ]


db = load_data()

st.sidebar.title("🔍 Filter Katalog")
kategori = st.sidebar.selectbox(
    "Pilih Jilid:",
    [
        "Semua Jilid",
        "Jilid 1: Kosmologi & Astrofisika",
        "Jilid 2: Geofisika & Meteorologi",
        "Jilid 3: Biologi & Embriologi",
    ],
)
search = st.sidebar.text_input("Cari Kata Kunci (misal: Pulsar, Bumi):")

filtered = db
if kategori != "Semua Jilid":
    filtered = [i for i in filtered if i["jilid"] == kategori]

if search:
    filtered = [
        i
        for i in filtered
        if search.lower() in i["sains"].lower()
        or search.lower() in i["terjemahan"].lower()
        or any(search.lower() in t.lower() for t in i["tags"])
    ]

st.write(f"Menampilkan **{len(filtered)}** ayat.")

for item in filtered:
    with st.expander(f"📖 {item['surah']} — {item['jilid']}", expanded=True):
        st.markdown(
            f"<h3 style='text-align: right; color: #1E3A8A;'>{item['arab']}</h3>",
            unsafe_allow_html=True,
        )
        st.write(f"**Terjemahan:** *\"{item['terjemahan']}\"*")
        st.info(f"💡 **Analisis Sains:** {item['sains']}")
