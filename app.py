# app.py
from flask import Flask, render_template

app = Flask(__name__)

# A dictionary to store the prayer texts. This now lives on the server.
prayers = {
    'hanuman-chalisa': """
Doha

Shri Guru Charan Saroj Raj,
Nij manu Mukuru Sudhari,
Baranau Rahuvar Bimal Jasu,
Jo Dayaku Phala Chari.

Buddhiheen Tanu Janike,
Sumirau Pavan Kumar,
Bal Buddhi Vidya Dehu Mohi,
Harahu Kalesh Vikaar.

Chaupai

Jai Hanuman Gyan Gun Sagar,
Jai Kapis Tihun Lok Ujagar.

Ramdoot Atulit Bal Dhama,
Anjani-putra Pavan-sut Nama.

Mahabir Bikram Bajrangi,
Kumati Nivar Sumati Ke Sangi.

Kanchan Baran Biraj Subesa,
Kanan Kundal Kunchit Kesa.

Hath Vajra Aur Dhvaja Biraje,
Kandhe Moonj Janeu Saje.

Sankar Suvan Kesari Nandan,
Tej Pratap Maha Jag Vandan.

Vidyavan Guni Ati Chatur,
Ram Kaj Karibe Ko Atur.

Prabhu Charitra Sunibe Ko Rasiya,
Ram Lakhan Sita Man Basiya.

Sukshma Roop Dhari Siyahi Dikhava,
Vikat Roop Dhari Lank Jarava.

Bhima Roop Dhari Asur Sanhare,
Ramachandra Ke Kaj Sanvare.

Laye Sanjivan Lakhan Jiyaye,
Shri Raghubir Harashi Ur Laye.

Raghupati Kinhi Bahut Badai,
Tum Mam Priye Bharat Hi Sam Bhai.

Sahas Badan Tumharo Jas Gave,
As Kahi Shripati Kanth Lagave.

Sanakadik Brahmadi Muneesa,
Narad Sarad Sahit Aheesa.

Yam Kuber Digpal Jahan Te,
Kavi Kovid Kahi Sake Kahan Te.

Tum Upkar Sugreevahi Keenha,
Ram Milaye Rajpad Deenha.

Tumharo Mantra Vibhishan Mana,
Lankeshwar Bhaye Sab Jag Jana.

Yug Sahastra Jojan Par Bhanu,
Leelyo Tahi Madhur Phal Janu.

Prabhu Mudrika Meli Mukh Maahi,
Jaladhi Langhi Gaye Achraj Naahi.

Durgam Kaj Jagat Ke Jete,
Sugam Anugraha Tumhre Tete.

Ram Duaare Tum Rakhvare,
Hot Na Aagya Binu Paisare.

Sab Sukh Lahai Tumhari Sarna,
Tum Rakshak Kahu Ko Dar Na.

Aapan Tej Samharo Aapai,
Teenon Lok Haank Te Kanpe.

Bhoot Pisaach Nikat Nahi Aavai,
Mahabir Jab Naam Sunavai.

Nase Rog Hare Sab Peera,
Japat Nirantar Hanumat Beera.

Sankat Te Hanuman Chudavai,
Man Kram Vachan Dhyan Jo Lavai.

Sab Par Ram Tapasvi Raja,
Tin Ke Kaj Sakal Tum Saja.

Aur Manorath Jo Koi Lavai,
Soi Amit Jivan Phal Pavai.

Charon Jug Partap Tumhara,
Hai Parsiddh Jagat Ujiyara.

Sadhu Sant Ke Tum Rakhvare,
Asur Nikandan Ram Dulare.

Ashta Siddhi Nau Nidhi Ke Data,
As Var Deen Janaki Mata.

Ram Rasayan Tumhare Pasa,
Sada Raho Raghupati Ke Dasa.

Tumhare Bhajan Ram Ko Pavai,
Janam Janam Ke Dukh Bisravai.

Ant Kaal Raghubar Pur Jai,
Jahan Janam Hari-Bhakt Kahai.

Aur Devta Chit Na Dharahi,
Hanumath Sei Sarva Sukh Karahi.

Sankat Kate Mite Sab Peera,
Jo Sumirai Hanumat Balbira.

Jai Jai Jai Hanuman Gosain,
Kripa Karahu Gurudev Ki Nyahin.

Jo Sat Bar Path Kare Koi,
Chutahi Bandi Maha Sukh Hoi.

Jo Yah Padhe Hanuman Chalisa,
Hoy Siddhi Sakhi Gaurisa.

Tulsidas Sada Hari Chera,
Keejai Nath Hriday Mein Dera.

Doha

Pavan Tanay Sankat Haran,
Mangal Murati Roop.
Ram Lakhan Sita Sahit,
Hriday Basahu Sur Bhoop.
    """,
    'tvamev-mata': """
Tvameva Maataa cha Pitaa tvameva.
Tvameva Bandhu cha Sakhaa tvameva.
Tvameva Vidyaa Dravinnam tvameva.
Tvameva Sarvam Mama Devadeva.
    """,
    'karage-vasate': """
Karagre vasate Lakshmi,
Karamadhye Saraswati.
Karamule tu Govinda,
Prabhate karadarshanam.
    """,
    'karpur-gauram': """
Karpur gauram karunavtaram
Sansar saram bhujagendra haram
Sada vasantam hridayarvinde
Bhavam bhavani sahitam namami.
    """,
    'janmangal-stotra': """
varṇi-veṣha-ramaṇīya-darshanam mandahāsa-ruchirāna-nāmbujam ।

Pūjitam suranarotta-mairmudā dharma-nandana-mahan vichintaye ॥4॥

Shrī-Kṛuṣhṇah Shrī-Vāsudevo Naranārāyaṇah prabhuhu ।

Bhakti-dharmātmajo-janmā Kṛuṣhṇo Nārāyaṇo harihi ॥5॥

Harikṛuṣhṇo Ghanashyāmo Dhārmiko Bhaktinandanah ।

Bṛuhad-vrata-dharah shuddho Rādhā-kṛuṣhṇeṣhṭa-daivatah ॥6॥

Marut-suta-priyah kālībhairavādyati-bhīṣhaṇah ।

Jitendriyo jitāhāras-tīvravairāgya āstikah ॥7॥

Yogeshvaro yoga-kalā-pravṛutti-rati-dhairyavān ।

Jnyānī paramahansashcha tīrtha-kṛuttair-thikārchitah ॥8॥

Kṣhamānidhihi sadon-nidro dhyāna-niṣhṭhas-tapah priyah ।

Siddheshvarah svatantrashcha brahma-vidyā-pravartakah ॥9॥

Pāṣhaṇḍo-chhedana-paṭuhu svasvarūpā-chala-sthitihi ।

Prashānta-mūrtir-nirdoṣho’sura-gurvādi-mohanah ॥10॥

Atikāruṇya-nayan Uddhavādhva-pravartakah ।

Mahāvratah sādhushīlah sādhu-vipra-prapūjakah ॥11॥

Ahinsa-yagna-prastotā sākāra-brahma-varṇanah ।

Swāminārāyaṇah Swāmī kāla-doṣha-nivārakah ॥12॥

Sachchhāstra-vyasanah sadyah-samādhi-sthiti-kārakah ।

Kṛuṣhṇārchā-sthāpana-karah kaulad-viṭ kali-tārakah ॥13॥

Prakāsha-rūpo nirdambhah sarva-jīva-hitāvahah ।

Bhakti-sampoṣhako vāgmī chatur-varga-fala-pradah ॥14॥

Nirmatsaro bhakta-varmā buddhi-dātā’tipāvanah ।

Abuddhihṛud-brahma-dhāma-darshakashchā-parājitah ॥15॥

Āsamudrānta satkīrtihi shrita-sansṛuti-mochanah ।

Udārah Sahajānandah sādhvī-dharma-pravartakah ॥16॥

Kandarpa-darpa-dalano vaiṣhṇava-kratu-kārakah ।

Panychāyatana-sammāno naiṣhṭhika-vrata-poṣhakah ॥17॥

Pragalbho nihspṛuhah satya-pratijnyo bhakta-vatsalah ।

Aroṣhaṇo dīrgha-darshī ṣhaḍ-ūrmi-vijaya-kṣhamah ॥18॥

Nirahankṛutira-droh ṛujuhu sarvopakārakah ।

Niyāma-kashcho-pashama-sthitir-vinayavān guruhu ॥19॥

Ajātavairī nirlobho mahāpuruṣh ātmadah ।

Akhaṇḍitārṣha-maryādo vyāsa-siddhānta-bodhakah ॥20॥

Mano-nigraha-yuktijnyo yama-dūta-vimochakah ।

Pūrṇakāmah satyavādī guṇagrāhī gatasmayah ॥21॥

Sadāchāra-priya-tarah puṇya-shravaṇa-kīrtanah ।

Sarva-mangala-sadrūpa-nānā-guṇa-vicheṣhṭitah ॥22॥
    """,
    'kararavindena': """
Kararavindena padaravindam,
Mukharavinde viniveshayantam.
Vatasya patrasya pute shayanam,
Balam Mukundam manasa smarami.
    """,
    'Jai sadguru swami':"""

Jai Sadguru Swami,
Prabhu Jai Sadguru Swami...
Sahajanand dayalu,
balavant Bahunami...Jai....1
Charan-saroj tamara vandu kar jodi,
Prabhu vandu kar jodi;
Charane chitt dharyathi,x2
dukh nakhya todi...Jai....2
Narayan narbhrata, dvij-kul tanu dhari,
Prabhu dvij-kul tanu dhari;
Pamar patit uddharya,x2
aganit narnari...Jai....3
Nitya nitya nautam lila karta Avinashi,
Prabhu karta Avinashi;
Adsath tirath charane,x2
koti Gaya Kashi...Jai....4
Purushottam pragat nu je darshan karshe,
Prabhu je darshan karshe;
Kal karma thi chhutti,x2
kutumb sahit tarshe...Jai....5
Aa avsar karuna nidhi, karuna bahu kidhi,
Vale karuna bahu kidhi;
Muktanand kahe mukti,x2
sugam kari sidhi...Jai....6
Jai Sadguru Swami,
Prabhu Jai Sadguru Swami;
Sahajanand dayalu,
balavant Bahunami...Jai....
    """
}

@app.route('/')
def home():
    """Renders the main HTML page with the list of prayer links."""
    return render_template('index.html', prayers=prayers.keys())

@app.route('/light')
def home_light():
    """Renders the light-mode main page with the list of prayer links."""
    return render_template('index_light.html', prayers=prayers.keys())

@app.route('/prayer/<prayer_name>')
def prayer_page(prayer_name):
    """Renders a new page with the text of the selected prayer."""
    prayer_text = prayers.get(prayer_name, "Prayer not found.")
    prayer_title = prayer_name.replace('-', ' ').title()
    return render_template('prayer_page.html', prayer_title=prayer_title, prayer_text=prayer_text, prayer_slug=prayer_name)

@app.route('/prayer-light/<prayer_name>')
def prayer_page_light(prayer_name):
    """Renders the light-mode page with the text of the selected prayer."""
    prayer_text = prayers.get(prayer_name, "Prayer not found.")
    prayer_title = prayer_name.replace('-', ' ').title()
    return render_template('prayer_page_light.html', prayer_title=prayer_title, prayer_text=prayer_text, prayer_slug=prayer_name)

if __name__ == '__main__':
    app.run(debug=True)
