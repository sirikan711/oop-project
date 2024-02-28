import streamlit as st

st.title('MY PIPO PIPO')
st.caption('List to Read')

st.markdown('## Manhwa')
choices = st.multiselect(
    'เลือกประเภทของ Manhwa ที่คุณสนใจ', ['Romance', 'Action', 'Fantasy', 'Horror', 'Drama', 'Comedy', 'Reincarnation', 'Time Travel', 'Adventure', 'Survival', 'Idol'])

# Romance Fantasy
if ('Romance' in choices or 'Fantasy' in choices) and all(choice in ['Romance', 'Fantasy'] for choice in choices):
    rm_fs = [
        {'image': 'manhwa_png/rm_fs00.jpeg',
         'caption': 'มาย เดม่อน',
         'markdown': 'ชื่ออังกฤษ : My Demon\n\n'
         '**โดโดฮี ทายาทสาวตัวแม่ของตระกูลแชบอล ผู้ไม่เคยเชื่อใจใคร และจองกูวอน ปีศาจหนุ่มผู้สมบูรณ์แบบ**ที่ใช้ชีวิตเยี่ยงนักล่าวิญญาณมากว่า 200 ปี แถมชอบมองมนุษย์เป็นเพียงสิ่งของไร้ค่า\n\n'
         'อยู่มาวันหนึ่ง พลังอันเป็นนิรันดร์ของจองวอนกูได้ย้ายไปอยู่กับโดโดฮี **เขาจึงต้องปกป้องเธอเพื่อหาวิธีนำพลังกลับคืนมา**',
         'web': 'Webtoon', 'link': 'https://www.webtoons.com/th/romantic-fantasy/my-demon/list?title_no=5978'},

        {'image': 'manhwa_png/rm_fs01.jpg',
         'caption': 'เจ้าสาวอสูรไร้ใจ',
         'markdown': 'ชื่ออังกฤษ : Married to a Beastly Duke\n\n'
         '**หญิงสาวคนหนึ่งที่ต้องแต่งงานกับ แกรนด์ดยุกสเตตัน** ผู้มีทรัพย์สินมากมาย และศักดินากว้างไกล แต่มีข่าวลือว่าเขาคือ**อสูรไร้ใจ**ที่ไม่มีทั้งเลือด และน้ำตา\n\n'
         '“แล้วทำไมถึงมาขอฉันแต่งงานกันล่ะ!?”',
         'web': 'Webtoon', 'link': 'https://www.webtoons.com/th/romantic-fantasy/married-to-a-beastly-duke/list?title_no=5907'},
         
        {'image': 'manhwa_png/rm_fs02.jpg',
         'caption': 'ช่างสามีเถอะ ฉันขอหาเงินดีกว่า',
         'markdown': 'ชื่ออังกฤษ : Forget My Husband, I’ll Go Make Money\n\n'
         '**อาลิสติเน่ ซิลวานุส องค์หญิงผู้มีเนตรจักรพรรดิที่สามารถมองเห็นอนาคตได้** เธอถูกคลุมถุงชนให้แต่งงานเพื่อเชื่อมความสัมพันธ์ระหว่างสองประเทศ แต่เธอก็รู้ว่าพ่อจะใช้เธอเป็นชนวนสงครามกับไอลูโก\n\n'
         'อาลิสติเน่จึงตั้งใจจะใช้การแต่งงานนี้ปลดปล่อยให้ตัวเองเป็นอิสระ และใช้ชีวิตอยู่บนกองเงินกองทอง **เพื่อการนั้นเธอจำเป็นต้องใช้อำนาจของทาร์คันคุ้มครองตัวเองจากคนของจักรพรรดิ** แล้วเธอจะสามารถบรรลุเป้าหมายได้หรือไม่',
         'web': 'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/ช่างสามีเถอะ_ฉันขอหาเงินดีกว่า/680?tab=episode'},
        
        {'image': 'manhwa_png/rm_fs03.jpg',
         'caption': 'ราตรีไร้เงา',
         'markdown': 'ชื่ออังกฤษ : Shadowless Night\n\n'
         '**โรซาลีน ที่บาดเจ็บหนักจากการปกป้ององค์ชายลำดับที่ 2 จากมือลอบสังหาร** ในขณะที่เธอกำลังนอนรอความตายอยู่นั้นก็ได้พบกับ **เงา** โรซาลีนจึงขอให้มันสานต่อความตั้งใจของตัวเองในการปกป้ององค์ชาย\n\n'
         'หลังจากโรซาลีนฟื้นขึ้นมา เธอทำตัวแปลกไปอย่างไม่เคยเป็นมาก่อน **หรือว่านั่นจะไม่ใช่เธอกันนะ**',
         'web':'Comico', 'link': 'https://www.comico.in.th/titles/3127'},

    ]
    for item in rm_fs:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Romance Drama
if ('Romance' in choices or 'Drama' in choices) and all(choice in ['Romance', 'Drama'] for choice in choices):
    rm_dm = [
        {'image': 'manhwa_png/rm_dm00.jpg',
         'caption': 'ถ้าไม่ร้องก็จงอ้อนวอนซะ',
         'markdown': 'ชื่ออังกฤษ : Cry, or Better Yet, Beg\n\n'
         '**นักล่านกรูปงาม แมทเธียส ฟอน เฮอร์ฮาร์ด** นายน้อยแห่งเมืองอาร์วิสที่งดงามราวกับสรวงสวรรค์ และ**นกแสนสวยที่ทำลายชีวิตอันแสนสมบูรณ์แบบของเขา เลย์ลา เลเวลีน**\n\n'
         'เรื่องราวอันน่าตื่นตาตื่นใจของความรัก, ความเกลียดชัง, การให้อภัย และการง้องอนกำลังจะได้รับการเปิดเผยออกมาให้ทุกคนได้รับรู้',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/romantic-fantasy/cry-or-better-yet-beg/list?title_no=5900'}
    ]
    for item in rm_dm:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Romance Drama Fantasy
if ('Romance' in choices or 'Fantasy' in choices or 'Drama' in choices) and all(choice in ['Romance', 'Fantasy', 'Drama'] for choice in choices):
    rm_dm_fs = [
        {'image': 'manhwa_png/rm_dm_fs00.jpg',
         'caption': 'ปลายทางวิวาห์นี้มีแต่ล่ม',
         'markdown':'ชื่ออังกฤษ : The Broken Ring : This Marriage Will Fail Anyway\n\n'
         'ชีวิตของ กัสเซล วัยหกขวบเปลี่ยนแปลงไปอย่างสิ้นเชิงหลัง อิเนส เด็กผู้หญิงวัยเดียวกันที่เลือกเขาเป็นคู่หมั้นด้วยเหตุผลที่ว่าเขารูปงามที่สุด **พอกัสเซลโตขึ้นก็พยายามใช้ชีวิตเพลิดเพลินกับอิสระแอบควงหญิงอื่น โดยหารู้ไม่ว่าอิเนสพอใจอย่างมาก**\n\n'
         'กัสเซลไม่เข้าใจในการกระทำของอิเนส **หลังจากได้เห็นท่าทีที่นิ่งเฉยของเธอ เขาจึงเริ่มเปลี่ยนไป จนเริ่มผิดแผนที่อิเนสวางไว้**',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/ปลายทางวิวาห์นี้มีแต่ล่ม/486?tab=episode'},

        {'image': 'manhwa_png/rm_dm_fs01.jpg',
         'caption': 'องค์หญิงสองหน้า',
         'markdown': 'ชื่ออังกฤษ : Two Sides of the Princess\n\n'
         '**เจ้าหญิงอโฟรเนีย ที่หมั้นหมายมาแล้วถึง 6 ครั้ง และถูกถอนหมั้นทั้ง 6 ครั้ง**เพราะคู่หมั้นพวกนั้นนอกใจอยู่เสมอ ทำให้ใครๆ ต่างก็คิดว่าองค์หญิงเป็นคนที่โง่เขลา\n\n'
         'แต่ที่จริงแล้วเธอมี 2 หน้า เพราะเธอตั้งใจจะแย่งบัลลังก์ และทวงทุกอย่างคืนจากพ่อเธอ',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/องค์หญิงสองหน้า/315?tab=episode'},

    ]
    for item in rm_dm_fs:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Romance Drama Fantasy Time Travel
if ('Romance' in choices or 'Fantasy' in choices or 'Drama' in choices or 'Time Travel' in choices) and all(choice in ['Romance', 'Fantasy', 'Drama', 'Time Travel'] for choice in choices):
    rm_dm_fs_tt = [
        {'image': 'manhwa_png/rm_dm_fs_tt00.jpg',
         'caption': 'เลดี้ผู้ห้ามแตะต้อง',
         'markdown':'ชื่ออังกฤษ : Solitary Lady\n\n'
         '**ฮิลลิส ที่ตายมาแล้วถึง 7 ครั้ง** ในวินาทีสุดท้ายพี่ชายยังขอให้ตายแทนน้องสาวที่ไม่ได้มีสายเลือดเดียวกันอีกต่างหาก\n\n'
         '**“ในชีวิตครั้งที่ 8 นี้ฉันจะไม่ปิดบังพลังอีกแล้ว คนพวกนั้นจะเป็นยังไงก็ช่าง”** เรื่องราวฮิลลิสที่กลับมาใช้ชีวิตใหม่อีกครั้ง',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/เลดี้ผู้ห้ามแตะต้อง/202?tab=episode'}

    ]
    for item in rm_dm_fs_tt:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Romance Comedy
if ('Romance' in choices or 'Comedy' in choices) and all(choice in ['Romance', 'Comedy'] for choice in choices):
    rm_cmd = [
        {'image': 'manhwa_png/rm_cmd00.jpg',
         'caption': 'โชคชะตานำพารัก',
         'markdown': 'ชื่ออังกฤษ : Maybe Meant to Be\n\n'
         'ฮันจีอา ฟรีแลนซ์สาววัย 32 ปี ที่เบื่อหน่ายกับคำถามเรื่องแต่งงานของพ่อแม่ บังเอิญพบกับเพื่อนสมัยเด็กอย่าง จินมินชอล หนุ่มเนิร์ดที่โดนคำถามจากพ่อแม่เรื่องนี้เช่นกัน\n\n'
         '**เพราะเหตุนี้ คนโสดทั้งสองจึงตัดสินใจจะหยุดคำถามเหล่านี้ด้วยการแต่งงานกัน** หรือว่านี่จะเป็นบุพเพสันนิวาส?',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/romance/maybe-meant-to-be/list?title_no=4951'}
    ]
    for item in rm_cmd:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Romance Comedy Fantasy
if ('Romance' in choices or 'Comedy' in choices or 'Fantasy' in choices) and all(choice in ['Romance', 'Comedy', 'Fantasy'] for choice in choices):
    rm_cmd_fs = [
        {'image': 'manhwa_png/rm_cmd_fs00.jpg',
         'caption': 'เอลิเซ่ แพทย์หญิงทะลุมิติ',
         'markdown': 'ชื่ออังกฤษ : Doctor Elise : The Royal Lady with the Lamp\n\n'
         '**ซงจีฮยอน ศัลยแพทย์มือฉมัง** ตั้งใจทุ่มเทชีวิตนี้ช่วยเหลือผู้คนเพื่อชดใช้ความผิดในอดีตชาติ แต่จู่ๆ เครื่องบินที่เธอนั่งเกิดเหตุระเบิด และเมื่อ**ฟื้นขึ้นมาก็พบว่าตัวเองอยู่ในร่างของเอลิเซ่ ตัวเธอในอดีตชาติ**\n\n'
         'การกลับมาของเธอจะสามารถเปลี่ยนแปลงอดีตที่เคยผิดพลาดไปได้หรือไม่',
         'web':'Comico', 'link': 'https://www.comico.in.th/titles/1319'},

        {'image': 'manhwa_png/rm_cmd_fs01.jpg',
         'caption': 'เจ้าหญิงผมดำกับเจ้าชายผมแดง',
         'markdown': 'ชื่ออังกฤษ : A Royal Princess with Black Hair\n\n'
         '**เจ้าหญิงยูรีเซียน และเจ้าชายคารูเอล ที่ต้องมาเป็นคู่หมั้นกันเพื่อแต่งงานทางการเมือง** แต่เนื่องจากทั้งคู่ไม่ได้มีความรักให้กันจึงตั้งใจจะหย่า\n\n'
         'พวกเขาจะหย่ากันได้สำเร็จหรือจะกลายมาเป็นคู่รักกันจริงๆ',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/romantic-fantasy/royal-princess/list?title_no=2103'}

    ]
    for item in rm_cmd_fs:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])


# Action
if 'Action' in choices and all(choice in ['Action'] for choice in choices):
    ac = [
        {'image': 'manhwa_png/ac00.jpg',
         'caption': 'ปีศาจกลับมาเรียน',
         'markdown': 'ชื่ออังกฤษ : Devil Returns to School Days\n\n'
         '**คิมฮยอนซอง นักเรียนดีเด่นที่ถูกพวกนักเลงในโรงเรียนพลักตกจากดาดฟ้าก่อนวันเรียนจบ** อาการของเขาอยู่ในขั้นโคม่า ไม่ตอบสนองใดๆ ยาวนานถึง 10 ปี\n\n'
         'อยู่มาวันหนึ่งเขาได้ย้อนเวลากลับไปในช่วงก่อนจะเกิดทุกอย่างขึ้น **“ฉันจะแก้แค้นพวกที่เคยกลั่นแกล้ง และพวกที่เมินเฉยให้หมด!”**',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/action/devil-goes-to-school/list?title_no=5456'},
        
        {'image': 'manhwa_png/ac01.jpg',
         'caption': 'หมาหัวเน่าเก๋าเกินไป',
         'markdown': 'ชื่ออังกฤษ : The Strongest Outcast\n\n'
         '**ชามูกยอล นักมวยฝีมือดีที่ถูกประธานหักหลัง จนเขากลายเป็นอัมพาต** แต่แล้ววิญญาณของชามูกยอลก็ได้เข้าไปสิงร่างของนักเรียนคนหนึ่งที่โดนบูลลี่\n\n'
         '**เขาจะกลับมาทำตามความฝัน และเอาคืนคนที่ทำให้เขาทุกข์ทรมาน**',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/action/the-strongest-outcast/list?title_no=5324'},

        {'image': 'manhwa_png/ac02.jpg',
         'caption': 'Study Group',
         'markdown': 'ชื่ออังกฤษ : Study Group\n\n'
         '**ยุนกามิน เด็กหนุ่มที่ต้องการเกรดดีๆ เพื่อที่เขาจะสามารถเข้าเรียนต่อในมหาลัยชั้นนำได้ ทว่าเขาไม่ได้มีหัวด้านการเรียนสักเท่าไหร่ ทางออกเดียวคือการ**เข้าเรียนในโรงเรียนสุดห่วยที่เต็มไปด้วยอันธพาล เพื่อที่จะได้มีเกรดดีๆ\n\n'
         'แต่**การทำตัวเป็นเด็กเนิร์ดตั้งใจเรียนท่ามกลางโรงเรียนที่เต็มไปด้วยอันธพาลนั้นไม่ใช่เรื่องง่าย** แล้วเขาจะใช้ชีวิตอยู่ในโรงเรียนนี้อย่างสงบ และสอบเข้ามหาลัยดีๆ ได้หรือไม่',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/action/studygroup/list?title_no=1595'},

        {'image': 'manhwa_png/ac03.jpg',
         'caption': 'อาชญากรวัยเยาว์',
         'markdown': 'ชื่ออังกฤษ : Juvenile Offender\n\n'
         '**อียุนซอง เยาวชนที่ต้องเข้าสถานพินิจเพราะกระทำความผิด** ทว่าเขาจงใจที่จะเข้าไปที่นั่น เพื่อล้างแค้นพวกคนชั่วที่มีกฎหมาบปกป้องอยู่',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/action/juvenile-offender/list?title_no=5457'}

    ]
    for item in ac:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Action Drama
if ('Action' in choices or 'Drama' in choices) and all(choice in ['Action', 'Drama'] for choice in choices):
    ac_dm = [
        {'image': 'manhwa_png/ac_dm00.jpg',
         'caption': 'พี่ชายสายบอดี้การ์ด',
         'markdown': 'ชื่ออังกฤษ : Teenage Mercenary\n\n'
         '**ยูอีจิน เด็กหนุ่มที่รอดชีวิตจากอุบัติเหตุเครื่องบินตก และใช้ชีวิตเป็นทหารรับจ้าง**โดยไร้ซึ่งความทรงจำมาตลอด\n\n'
         'จนกระทั่งความทรงจำเขาเริ่มกลับมา และด้วยความช่วยเหลือจากทหารเกาหลีที่ร่วมเสี่ยงเป็นเสี่ยงตายกันมา **เขาได้กลับมาใช้ชีวิตกับคุณปู่ และน้องสาวที่เหลือเพียงคนเดียวอีกครั้งในฐานะเด็กม.ปลาย แต่ชีวิตที่สงบสุขมันไม่ได้มาง่ายๆ นี่สิ**',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/action/high-school-soldier/list?title_no=2438'},

        {'image': 'manhwa_png/ac_dm01.jpg',
         'caption': 'Y2K จงเจริญ',
         'markdown': 'ชื่ออังกฤษ : Ulzzang Generation\n\n'
         '**พัคชงอิล นักเรียน ม.ปลาย ได้รับการเลี้ยงดูจากเพื่อนสนิทของพ่อ** ซึ่งพ่อของพัคชองอิลหายตัวไปตั้งแต่เขายังเด็ก วันหนึ่งเขาก็ได้ข่าวว่าพ่อตายแล้ว จึงต้องแวะไปที่สถานีตำรวจเพื่อนำของใช้ของพ่อกลับมาด้วย\n\n'
         'ในบรรดาข้าวของเหล่านั้น มีโทรศัพท์เก่าๆ ที่เหมือนจะไม่มีแบตแล้ว แต่จู่ๆ ก็มีคนโทรเข้ามา แล้วบอกว่านี่เป็นโทรศัพท์ของเขาอยากจะขอคืน เมื่อนัดเจอกัน **พัคชงอิลก็ต้องตกใจเพราะได้เจอกับพ่อที่ทิ้งเขาไป “นี่ฉันย้อนอดีตมาหรอเนี่ย!?”**',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/action/ulzzang-generation/list?title_no=6031'},

        {'image': 'manhwa_png/ac_dm02.jpg',
         'caption': 'เหยื่ออย่างผมต้องรอด',
         'markdown': 'ชื่ออังกฤษ : To Not Die\n\n'
         '**อิมดาจุน ถูกบูลลี่ที่โรงเรียนจนชินชา และตัดสินใจจะฆ่าตัวตาย** แต่เขาก็ได้เปลี่ยนใจไปตามฆ่าพวกที่เคยแกล้งเขาแทน หลักจากแก้แค้นสำเร็จชีวิตเขาก็ไม่เหมือนเดิม ไม่มีโรงเรียนให้ไป ไม่มีบ้านให้กลับ\n\n'
         'ตอนนี้เขาต้องเอาตัวรอดจากชีวิตข้างถนนอันโหดร้ายให้ได้',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/action/to-not-die/list?title_no=3390'},

    ]
    for item in ac_dm:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Action Drama Comedy
if ('Action' in choices or 'Drama' in choices or 'Comedy' in choices) and all(choice in ['Action', 'Drama', 'Comedy'] for choice in choices):
    ac_dm_cmd = [
        {'image': 'manhwa_png/ac_dm_cmd00.jpg',
         'caption': 'Lookism',
         'markdown': 'ชื่ออังกฤษ : Lookism\n\n'
         '**สังคมที่ให้ค่ากับรูปลักษณ์ภายนอก ทำให้ พัคฮยองซอก เด็กหนุ่มที่มีรูปร่างอ้วน และฐานะยากจนตกเป็นเป้าของการบูลลี่**จนต้องทำเรื่องย้ายโรงเรียน\n\n'
         'แต่แล้วเขากลับ**ตื่นขึ้นมาในร่างของชายหนุ่มหน้าตาดี โดยที่มีร่างเดิมของเขานอนอยู่ข้างๆ** เขาจึงต้องใช้ชีวิตในร่างหนุ่มรูปงามตอนกลางวัน และร่างหนุ่มอ้วนในตอนกลางคืน',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/action/lookism/list?title_no=576'},
    ]
    for item in ac_dm_cmd:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Action Romance
if ('Action' in choices or 'Romance' in choices) and all(choice in ['Action', 'Romance'] for choice in choices):
    ac_rm = [
        {'image': 'manhwa_png/ac_rm00.jpg',
         'caption': 'ไวท์ บลัด',
         'markdown': 'ชื่ออังกฤษ : White Blood\n\n'
         '**พัคฮายัน แวมไพร์เลือดบริสุทธิ์ที่มีจิตใจอ่อนโยน** และมีความหวังว่าอยากจะใช้ชีวิตอยู่ร่วมกันกับมนุษย์อย่างสงบสุข **แต่มนุษย์นั้นกลับหวาดกลัวและเกลียดชังแวมไพร์ยิ่งกว่าอะไร**\n\n'
         'ความหวังของพัคฮายันจะมีทางเป็นจริงได้หรือไม่',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/action/white-blood/list?title_no=1948'},
    ]
    for item in ac_rm:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Action Fantasy
if ('Action' in choices or 'Fantasy' in choices) and all(choice in ['Action', 'Fantasy'] for choice in choices):
    ac_fs = [
        {'image': 'manhwa_png/ac_fs00.jpg',
         'caption': 'ดันเจี้ยนโอดิสซีย์',
         'markdown': 'ชื่ออังกฤษ : Dungeon Odyssey\n\n'
         '**คิมจินอู หนึ่งในดันเจี้ยนเบบี้ที่มีร่างกายแข็งแกร่ง และพลังพิเศษ**จากการเติบโตมาด้วยน้ำนมของบีสต์ เขาถูกปล่อยตัวออกมาจากเขาวงกตเนื่องจากมนุษย์ชนะในสงคราม คิมอูจินจึงพยายามใช้ชีวิตใหม่กับครอบครัว\n\n'
         'วันหนึ่ง**เขาอยากหาเงินให้ได้มากๆ เพื่อความเป็นอยู่ที่ดีของครอบครัว จึงตัดสินใจกลับเข้าไปในเขาวงกตอีกครั้ง**เพื่อ ดาวน์เจม อัญมณีอันมีค่าที่ทำเงินได้มหาศาล',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/DUNGEON_ODYSSEY/574?tab=episode'},

        {'image': 'manhwa_png/ac_fs01.jpg',
         'caption': 'อดีตบอสหอคอย',
         'markdown': 'ชื่ออังกฤษ : I Was the Final Boss\n\n'
         '**บาโฟเมต บอสแห่งหอคอยห้วงลึก ที่กำลังเบื่อหน่ายกับการต่อสู้แบบเดิมๆ** วันหนึ่งมีฮันเตอร์ผู้แข็งแกร่งปรากฎขึ้นต่อหน้าเขา นั่นยิ่งทำให้เขารู้สึกตื่นเต้นกับการมีอยู่ของมนุษย์\n\n'
         'วันหนึ่ง**เขาได้กลายเป็นมนุษย์ แต่เนื้อแท้ข้างในก็ยังเป็นปีศาจ**',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/fantasy/i-was-the-final-boss/list?title_no=5587'},
        
        {'image': 'manhwa_png/ac_fs02.jpg',
         'caption': 'อ่านชะตาวันสิ้นโลก',
         'markdown': 'ชื่ออังกฤษ : Omniscient Reader\n\n'
         '**ชีวิตของพนักงานออฟฟิศธรรมดาคนหนึ่งชื่อว่า คิมดกจา ที่เปลี่ยนไปในชั่วพริบตา**\n\n'
         'เนื่องจากตอนที่เขากำลังนั่งรถไฟฟ้ากลับบ้าน ได้เกิดเหตุการณ์ประหลาดขึ้น โลกทั้งโลกกำลงจะล่มสลาย แต่เหตุการณ์นี้กลับคุ้นเหมือนเคยเจอที่ไหน **“นี่มันนิยายที่เราอ่านอยู่คนเดียวนี่!?”**',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/fantasy/omniscient-reader/list?title_no=2106'},
        
        {'image': 'manhwa_png/ac_fs03.jpg',
         'caption': 'หลังวันสิ้นโลก',
         'markdown': 'ชื่ออังกฤษ : The World After the Fall\n\n'
         'เมื่อ**โลกได้บังคับให้มนุษย์ต้องกลายเป็น ทาวเวอร์วอล์กเกอร์** เพื่อทำลายหอคอยประหลาดที่อยู่ใจกลางเมือง ความหวังของมวลมนุษยชาติแทบจะน้อยนิด\n\n'
         '**มีวอล์กเกอร์คนหนึ่งสามารถพิชิตหอคอยได้สำเร็จ ทว่าความเชื่อที่เขามีต่อโลกดูเหมือนจะไม่มีค่าอีกต่อไป** เกิดอะไรขึ้นกับเขากันนะ',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/fantasy/the-world-after-the-fall/list?title_no=4205'},

        {'image': 'manhwa_png/ac_fs04.jpg',
         'caption': 'Solo Leveling',
         'markdown': 'ชื่ออังกฤษ : Only I Level Up\n\n'
         '**โลกที่มีการปรากฏตัวของ เกต** ประตูเชื่อมมิติที่ภายในเต็มไปด้วยมอนสเตอร์มากมาย และ**ผู้คนในโลกที่ถูกปลุกพลังจะกลายเป็น ฮันเตอร์** ที่สามารถต่อกรกับพวกมันได้\n\n'
         '**ซองจินอู ฮันเตอร์สุดกากที่กลายมาเป็นฮันเตอร์ที่แข็งแกร่งที่สุดของมนุษยชาติ** หลังจากรอดชีวิตจากเหตุการณ์ดับเบิลดันเจี้ยน',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/solo_leveling/48?tab=episode'},

    ]
    for item in ac_fs:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Action Fantasy Adventure
if ('Action' in choices or 'Fantasy' in choices or 'Adventure' in choices) and all(choice in ['Action', 'Fantasy', 'Adventure'] for choice in choices):
    ac_fs_ad = [
        {'image': 'manhwa_png/ac_fs_ad00.jpg',
         'caption': 'หวนคืนสู่ฮวาซาน',
         'markdown': 'ชื่ออังกฤษ : Return of The Blossoming Blade\n\n'
         '**ศิษย์รุ่น 13 แห่งฮวาซาน ผู้ปลิดชีพเทพมารที่รุกรานทั่วพิภพลงได้** และเขาได้สิ้นใจบนจุดสูงสุดของยอดเขา\n\n'
         'เมื่อลืมตาตื่นขึ้น เขากลับกลายเป็นยาจกไร้กำลังซะอย่างนั้น **“นี่ข้าเกิดใหม่เป็นขอทานหรือนี่!?”**',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/fantasy/return-of-the-blossoming-blade/list?title_no=3029'},

        {'image': 'manhwa_png/ac_fs_ad01.jpg',
         'caption': 'มหาจอมเวทผู้กลับมาอีกครั้งหลัง 4000 ปี',
         'markdown': 'ชื่ออังกฤษ : The Archmage Returns After 4000 Years\n\n'
         '**ลูคัส โทรว์แมน มหาจอมเวทผู้ยิ่งใหญที่ถูกลงโทษ**เพราะไปท้าทายพระเจ้า จึงถูกกักขังเป็นเวลายาวนานถึง 4000 ปี\n\n'
         'หลังจากนั้น เขาได้เข้ามาอยู่ในร่างของนักเรียนผู้อ่อนแออย่าง เฟรย์ เบลด ที่ถูกเรียกว่าความอัปยศของอะคาเดมี **มหาจอมเวทจะใช้ร่างนี้แก้แค้นพวกที่จับเขาขังถึง 4000 ปีได้ไหม**',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/มหาจอมเวทผู้กลับมาอีกครั้งหลัง_4000_ปี/10?tab=episode'},

        {'image': 'manhwa_png/ac_fs_ad02.jpg',
         'caption': 'ฮีลเลอร์กำมะลอ',
         'markdown': 'ชื่ออังกฤษ : Life of a Quack Healer\n\n'
         '**คังซึงฮยอน ตื่นขึ้นมาในโลกแฟนตาซีที่เขาได้รับมอบหมายให้เป็นฮีลเลอร์ ทว่าสกิลติดตัวเขากลับไม่ใช่พลังฮีล** แม้ว่าเขาจะมีสกิลที่เก่งกาจอื่นๆ อีกมากมาย แต่ถ้าฮีลไม่ได้แล้วจะใช้ชีวิตในฐานะฮีลเลอร์ยังไง?',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/fantasy/life-of-a-quack-healer/list?title_no=5539'},

        {'image': 'manhwa_png/ac_fs_ad03.jpg',
         'caption': 'มาย S-คลาส ฮันเตอร์',
         'markdown': 'ชื่ออังกฤษ : My S-Class Hunters\n\n'
         '**ฮันยูจิน ที่ยอมลาออกจากโรงเรียนเพื่อหาเงินเลี้ยงดูน้องชาย วันหนึ่ง เกต ที่เชื่อมต่อกับดันเดี้ยนของโลกอื่นได้ปรากฏขึ้น** ท่ามกลางความโกลาหลก็ได้มีบางคนถูกปลุกพลังหลังประจันหน้ากับสัตว์ประหลาด และกลายเป็นฮันเตอร์\n\n'
         '**น้องชายของ ฮันยูจิน ได้กลายเป็นฮันเตอร์ระดับ S แต่เขากลับอยู่แค่ระดับ F** เท่านั้น ต่อไปนี้เขาจะเป็นอย่างไรต่อไป',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/fantasy/my-sclass-hunters/list?title_no=3882'},

    ]
    for item in ac_fs_ad:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Action Fantasy Adventure Time Travel
if ('Action' in choices or 'Fantasy' in choices or 'Adventure' in choices or 'Time Travel' in choices) and all(choice in ['Action', 'Fantasy', 'Adventure', 'Time Travel'] for choice in choices):
    ac_fs_ad_tt = [
        {'image': 'manhwa_png/ac_fs_ad_tt00.jpg',
         'caption': 'พลทหารโครงกระดูกผู้มิอาจปกป้องดันเจี้ยน',
         'markdown': 'ชื่ออังกฤษ : The Skeleton Soldier Failed to Defend the Dungeon\n\n'
         '**พลทหารโครงกระดูก มอนสเตอร์ที่ถูกฆ่าทิ้งอย่างไร้ค่า โดยไม่สามารถปกป้องผู้เป็นนายได้** เขาคิดว่าตัวเองคงตายไปทั้งอย่างนั้น แต่เขาได้ย้อนเวลากลับไป 20 ปีก่อน ด้วยพลังของผู้ใช้ความตาย\n\n'
         '**“ในครั้งนี้ข้ามองเห็นหน้าต่างสถานะที่คนอื่นมองไม่เห็น และไม่ว่าตายกี่ครั้งข้าก็จะฟื้นขึ้นมา!”**',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/พลทหารโครงกระดูกผู้มิอาจปกป้องดันเจี้ยน/219?tab=episode'},

        {'image': 'manhwa_png/ac_fs_ad_tt01.jpg',
         'caption': 'นักล่าพลีชีพ ระดับ SSS',
         'markdown': 'ชื่ออังกฤษ : SSS-Class Revival Hunter\n\n'
         '**คิมกงจา ฮันเตอร์ปลายแถวระดับ F ได้ครอบครองสกิลระดับ S+** ที่ทำให้เขาสามารถก๊อบปี้สกิลของฮันเตอร์คนอื่นได้ โดยมี**เงื่อนไขเพียงอย่างเดียวคือเขาต้องตาย**',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/นักล่าพลีชีพ_ระดับ_SSS/98?tab=episode'},

    ]
    for item in ac_fs_ad_tt:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])


# Action Fantasy Drama
if ('Action' in choices or 'Fantasy' in choices or 'Drama' in choices) and all(choice in ['Action', 'Fantasy', 'Drama'] for choice in choices):
    ac_fs_dm = [
        {'image': 'manhwa_png/ac_fs_dm00.jpg',
         'caption': 'สงครามนักรบผู้หวนคืน',
         'markdown': 'ชื่ออังกฤษ : The Warrior is Back\n\n'
         'พัคจองอู นักรบผู้กอบกู้ต่างโลก ได้มีโอกาสย้อนกลับมายังโลกเดิมเพื่อแก้แค้น คิมมินซู นักรบผู้ฆ่าครอบครัวของเขา\n\n'
         '**ในโลกที่ปราศจากความสงบสุข และเต็มไปด้วยการนองเลือด สองนักรบต้องมาห่ำหั่นกันเอง**',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/fantasy/the-warrior-is-back/list?title_no=3302'},
    ]
    for item in ac_fs_dm:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Fantasy
if 'Fantasy' in choices and all(choice in ['Fantasy'] for choice in choices):
    fs = [
        {'image': 'manhwa_png/fs00.jpg',
         'caption': 'ผู้พิชิตเกมป้องกันฐาน',
         'markdown': 'ชื่ออังกฤษ : I Became the Tyrant of a Defence Game\n\n'
         '**ชายหนุ่มคนหนึ่ง ที่สามารถเอาชนะเกมปกป้องอณาจักรได้** ซึ่งเป็นเกม RPG แนวป้องกันฐานตะลุยดันเจี้ยน\n\n'
         'ทว่าพอเขาตั้งสติได้ก็หลุดเข้ามาอยู่ในเกมซะแล้ว แถมยังเป็นด่านแสนยากอีกต่างหาก **“ฉันจะเอาชนะมันให้ได้ ไอ้เกมเสงเครงนี่น่ะ!”**',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/fantasy/i-became-the-tyrant-of-a-defense-game/list?title_no=3812'},

        {'image': 'manhwa_png/fs01.jpg',
         'caption': 'รีเทิร์นเซอร์ไววัล',
         'markdown': 'ชื่ออังกฤษ : Return Survival\n\n'
         '**โยฮัน ที่ได้ย้อนเวลากลับไปเมื่อ 6 ปีก่อนที่ซอมบี้จะปรากฎตัวขึ้น** แต่เหตุการณ์กลับไม่เป็นเหมือนในอดีต เมื่อทุกอย่างเกิดเร็วขึ้นกว่าที่ควรจะเป็น\n\n'
         'โลกถึงคราวอวสาน เพราะ**นอกจากจะต้องเอาชีวิตรอดจากซอมบี้แล้ว ยังต้องคอยระวังคนชั่วอีก** โยฮันจะเอาชีวิตรอดจากสองอย่างนี้ไปได้อย่างไร',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/Return_Survival/113?tab=episode'},

    ]
    for item in fs:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Fantasy Adventure
if ('Fantasy' in choices or 'Adventure' in choices) and all(choice in ['Fantasy', 'Adventure'] for choice in choices):
    fs_ad = [
        {'image': 'manhwa_png/fs_ad00.jpg',
         'caption': 'ยอดสถาปนิกผู้พิทักษ์อาณาจักร',
         'markdown': 'ชื่ออังกฤษ : The Greatest Estate Developer\n\n'
         '**คิมซูโฮ นักศึกษาวิศวกรรมโยธา ที่ได้หลุดเข้ามาอยู่ในนิยายแฟนตาซีที่อ่านเมื่อคืน** ซึ่งตัวละครที่เขาเข้ามาสวมร่างนั้นคือ ลอยด์ ฟรอนเทร่า ชนชั้นสูงที่ขี้เกียจตัวเป็นขนชอบเมาหัวราน้ำตลอด แถมครอบครัวก็ยังเป็นหนี้อีกต่างหาก\n\n'
         '**ซูโฮจึงประยุกต์ใช้ความรู้ทางด้านวิศวกรรมที่มีอยู่ เพิ่อเริ่มต้นชีวิตใหม่อย่างใสสะอาด** พร้อมได้รับความช่วยเหลือจากเจ้าแฮมสเตอร์ยักษ์ อัศวิน และเวทมนตร์ของโลกใบนี้',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/fantasy/the-greatest-estate-developer/list?title_no=4646'},
    ]
    for item in fs_ad:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Fantasy Drama
if ('Fantasy' in choices or 'Drama' in choices) and all(choice in ['Fantasy', 'Drama'] for choice in choices):
    fs_dm = [
        {'image': 'manhwa_png/fs_dm00.jpg',
         'caption': 'เมื่อมีเกตเปิดในวันแรกที่ผมรับตำแหน่ง',
         'markdown': 'ชื่ออังกฤษ : A Monstrous First Day\n\n'
         '**ฮันซึงมุน ได้ลงสมัครเลือกตั้ง**ทั้งที่ก็ไม่มีตวามเป็นไปได้ว่าจะชนะ **แต่กลับชนะซะอย่างงั้น** ทว่า**ในวันที่เขาเข้ารับตำแหน่งกลับเกิดเรื่องโกลาหลขึ้น** ปีศาจหลั่งไหลเข้ามาโจมตีผู้คน\n\n'
         'เขาจะทำอย่างไรต่อไป และจะจัดการกับสถานการณ์นี้ยังไง',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/เมื่อมีเกตเปิดในวันแรกที่ผมรับตำแหน่ง/610?tab=episode'},

    ]
    for item in fs_dm:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Fantasy Comedy Time Travel
if ('Fantasy' in choices or 'Comedy' in choices or 'Time Travel' in choices) and all(choice in ['Fantasy', 'Comedy', 'Time Travel'] for choice in choices):
    fs_cmd_tt = [
        {'image': 'manhwa_png/fs_cmd_tt00.jpg',
         'caption': 'ใครแตะต้องน้องฉันมันต้องตาย',
         'markdown': 'ชื่ออังกฤษ : Touch My Little Brother and You’re Dead\n\n'
         'โรซาเลตต์ พี่สาวของ แอสเทรีออน นายเอกในนิยาย BL ที่ถูกผู้ชายเฮงซวยในเรื่องย่ำยีจนต้องฆ่าตัวตาย ซึ่งเธอก็ไม่ได้อยากแทรกแซงเรื่องราวหรอก **แต่ทุกครั้งที่น้องชายตาย เธอก็ย้อนเวลากลับมาช่วงอายุ 16 ปีตลอด**\n\n'
         'โรซาเลตต์ทนไม่ไหวอีกต่อไป **“ไม่ว่าใครหน้าไหนที่กล้ามายุ่งกับน้องชายฉัน ฉันจะฆ่าให้หมดเลย!”**',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/ใครแตะน้องฉัน_มันต้องตาย/303?tab=episode'},
    ]
    for item in fs_cmd_tt:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])



# Horror
if 'Horror' in choices and all(choice in ['Horror'] for choice in choices):
    hr = [
        {'image': 'manhwa_png/hr00.jpg',
         'caption': 'รีเซตเตอร์',
         'markdown': 'ชื่ออังกฤษ : Reseter\n\n'
         '**ชายคนหนึ่งที่สามารถรีเซตชีวิตผ่านทางความตายได้** ซึ่งเมื่อลืมตาตื่นขึ้นมาก็จะไปอยู่ในร่างคนอื่นแบบแรนด้อม วันหนึ่งผู้จัดการเซิร์ฟได้ยื่นข้อเสนอให้เขาหยุดการรีเซตพร้อมกับมอบร่างที่ดีที่สุดให้\n\n'
         '**เขาได้มาใช้ชีวิตในฐานะ โจยูล จนแต่งงานมีลูกใช้ชีวิตอย่างสงบสุข ทว่าก็ได้มีเหตุการณ์ประหลาดพรากภรรยา และลูกของเขาไป** เนื่องจากมีรีเซตเตอร์อีกคนสร้างลัทธินิรันดรขึ้นมาแล้วเผยแพร่ความเชื่อผิดๆ ให้คนมาเข้าร่วม โจยูลจึงแฝงตัวเข้าไปในลัทธิเพื่อจบเรื่องนี้ และเพื่อความสุขที่เขาตามหามานาน',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/Reseter/369?tab=episode'},

        {'image': 'manhwa_png/hr01.jpg',
         'caption': 'สัตว์ปีกสยองขวัญ',
         'markdown': 'ชื่ออังกฤษ : Bird Phobia\n\n'
         '**ฮันซอลมิน หัวหน้าแผนกที่เป็นโรคกลัวนก** เขามองเห็นผู้จัดการคนใหม่เป็นนกเขาจึงรู้สึกกลัว หรือที่จริงแล้วผู้จัดการอาจจะไม่ใช่คน\n\n'
         'จนเกิดเป็น**เรื่องราวสุดระทึกระหว่างมนุษย์กับสัตว์ประหลาดครึ่งนกครึ่งคน**ที่เรียกว่า ฮาเปีย',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/สัตว์ปีกสยองขวัญ/59?tab=episode'},

        {'image': 'manhwa_png/hr02.jpg',
         'caption': 'เทส ออฟ เฮอเรอร์',
         'markdown': 'ชื่ออังกฤษ : Tastes of Horror\n\n'
         '**มันฮวาที่รวมเรื่องสั้นสยองขวัญจากนักเขียน และนักวาดหลายคน** ทำให้เนื้อเรื่องในแต่ละตอนชวนสนุก ตื่นเต้น เร้าใจ',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/TASTES_OF_HORROR/513?tab=episode'},

    ]
    for item in hr:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Horror Drama
if ('Horror' in choices or 'Drama' in choices) and all(choice in ['Horror', 'Drama'] for choice in choices):
    hr_dm = [
        {'image': 'manhwa_png/hr_dm00.jpg',
         'caption': 'ปีศาจอยู่ระหว่างเรา',
         'markdown': 'ชื่ออังกฤษ : No Devil\n\n'
         'มันฮวารวมเรื่องระทึกขวัญของ **เหล่ามนุษย์ ที่ต้องพบเจอกับปีศาจ** เป็นดั่งฝันร้ายสุดหลอน',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/thriller/no-devil/list?title_no=5404'},
    ]
    for item in hr_dm:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Horror Action Drama
if ('Horror' in choices or 'Action' in choices or 'Drama' in choices) and all(choice in ['Horror', 'Action', 'Drama'] for choice in choices):
    hr_ac_dm = [
                {'image': 'manhwa_png/hr_ac_dm00.jpg',
         'caption': 'สวีทโฮม',
         'markdown': 'ชื่ออังกฤษ : Sweet Home\n\n'
         '**ฮยอนซู ที่สูญเสียครอบครัวทั้งหมดไปในอุบัติเหตุ** เขาได้ย้ายไปอยู่อพาร์ทเมนต์ที่มีค่าเช่าราคาถูก และเก็บตัวหลบหนีจากสังคม พร้อมกับตัดสินใจกำหนดวันฆ่าตัวตายให้กับตัวเอง\n\n'
         'วันหนึ่งได้เกิดเหตุการณ์ประหลาดขึ้น **มีปีศาจออกไล่ฆ่าคน และคนที่ตายก็กลายเป็นปีศาจ** ฮยอนซู จะทำยังไงจะเอาชีวิตรอดหรือตายไปแบบที่เคยคิดไว้ดี',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/thriller/sweet-home/list?title_no=1257'},
    ]
    for item in hr_ac_dm:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Horror Time Travel Survival
if ('Horror' in choices or 'Time Travel' in choices or 'Survival' in choices) and all(choice in ['Horror', 'Time Travel', 'Survival'] for choice in choices):
    hr_tt_sv = [
        {'image': 'manhwa_png/hr_tt_sv00.jpg',
         'caption': 'โรแมนซ์ต้องรอด!',
         'markdown': 'ชื่ออังกฤษ : Surviving Romance\n\n'
         '**ชาเอริน กำลังเพลิดเพลินไปกับชีวิตในนิยายโรแมนซ์เล่มโปรด** ที่เธอได้กลายเป็นนางเอกในนิยายเรื่องนี้ ชีวิตช่างดูดี ทุกอย่างดูจะปูทางให้เธอได้เจอกับความแฮปปี้ไปตลอด\n\n'
         'แต่แล้วนิยายเรื่องนี้กลับกลายเป็นแนวอื่น เมื่อเกิดเหตุการณ์ไม่คาดฝันขึ้นจน**ชาเอรินตาย และกลับมาเริ่มใหม่ตั้งแต่ต้นซ้ำแล้วซ้ำเล่า** เธอจะทำอย่างไรกับห้วงเวลาที่หยุดไม่ได้นี้',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/fantasy/survived-romance/list?title_no=2837'},
    ]
    for item in hr_tt_sv:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])


# Reincarnation Fantasy
if ('Reincarnation' in choices or 'Fantasy' in choices)and all(choice in ['Reincarnation', 'Fantasy'] for choice in choices):
    rc_fs = [
        {'image': 'manhwa_png/rc_fs00.jpg',
         'caption': 'อันธพาลแห่งตระกูลเคานต์',
         'markdown': 'ชื่ออังกฤษ : Lout of Count’s Family\n\n'
         '**คิมรกซู ได้เข้าไปอยู่ในร่างอันธพาลตัวร้ายในนิยายชื่อว่า เคล** เขาจึงตั้งใจจะมีชีวิตรอดโดยไม่ถูกตัวเอกของเรื่อง ชเวฮัน อัดจนเละเหมือนในนิยาย\n\n'
         'เขาจะมีชีวิตรอด ไม่เจ็บป่วย และใช้ชีวิตอย่างสงบสุขได้หรือไม่',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/อันธพาลแห่งตระกูลเคานต์/14?tab=episode'},

        {'image': 'manhwa_png/rc_fs01.jpg',
         'caption': 'จอมเวทเกิดใหม่ในรอบ 66666 ปี',
         'markdown': 'ชื่ออังกฤษ : 66,666 Years : Advent of the Dark Mage\n\n'
         '**ดิอาโบล โวลพีร์ จอมเวทแห่งศาสตร์มืดผู้ยิ่งใหญ่ ตกหลุมพรางของเหล่า 12 เทพสวรรค์ จนต้องถูกผนึกตลอดกาล**\n\n'
         'หลังจาก หกหมื่นหกพันหกร้อยหกสิบหก ปีผ่านไป **จอมเวทที่น่าเกรงขามมากที่สุดในประวัติศาสตร์ได้ลงมาจุติบนโลก** ในฐานะบุตรชายหัวแก้วหัวแหวนของ เอิร์ลเวลตัน อีกครั้ง',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/fantasy/66666-years-advent-of-the-dark-mage/list?title_no=3680'},

    ]
    for item in rc_fs:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Reincarnation Action Fantasy
if ('Reincarnation' in choices or 'Action' in choices or 'Fantasy' in choices) and all(choice in ['Reincarnation', 'Action', 'Fantasy'] for choice in choices):
    rc_ac_fs = [
        {'image': 'manhwa_png/rc_ac_fs00.jpg',
         'caption': 'เกิดใหม่ในร่างดยุก',
         'markdown': 'ชื่ออังกฤษ : Returned as the Duke\n\n'
         '**ดยุกอารอน โอรสของอดีตจักรพรรดิ ผู้ที่ได้รับพลังพิเศษ พรแห่งมังกร** ต้องออกมาจากจักรวรรดิเพื่อใช้ชีวิตอย่างเจียมตัวในดินแดนอันไกลโพ้น แม้ว่าเขาจะไม่ย่างกรายเข้าไปยุ่งกับจักรวรรดิแล้ว แต่จักรพรรดิเจอรอนผู้มีศักดิ์เป็นอากลับไม่ยอมรามือจากเขา\n\n'
         'คืนหนึ่ง**จักรพรรดิเจอรอนได้ส่งกองทัพมาถล่มดินแดนของดยุกอารอนจนล่มสลาย** ซึ่งพ่อบ้านชราคนหนึ่งได้เสียชีวิตจากเหตุการณ์นั้นด้วย ทว่าในตอนที่**ชายชรากำลังคิดว่าทุกอย่างมันจบแล้ว เขาก็รู้สึกตัวในร่างของท่านดยุกอารอน เมื่อ 20 ปีก่อน**',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/fantasy/return-as-the-duke/list?title_no=5403'},
    ]
    for item in rc_ac_fs:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])


# Idol Reincarnation Time Travel Drama
if ('Idol' in choices or 'Reincarnation' in choices or 'Time Travel' in choices or 'Drama' in choices)and all(choice in ['Idol', 'Reincarnation', 'Time Travel', 'Drama'] for choice in choices):
    id_rc_tt_dm = [
        {'image': 'manhwa_png/id_rc_tt_dm00.jpg',
         'caption': 'เดบิวต์ หรือ ตาย',
         'markdown': 'ชื่ออังกฤษ : Debut or Die!\n\n'
         '**รยูกอนอู หนุ่มอายุ 29 ปี ผู้ที่มีชีวิตไม่รุ่งเอาซะเลย** วันหนึ่งหลังจากที่เขาเมาแล้วหลับไป **พอตื่นขึ้นมาก็พบว่าตัวเองเข้ามาสวมร่างเด็กหนุ่มที่ชื่อ พัคมุนแด แถมยังย้อนเวลากลับมา 3 ปี**\n\n'
         'ขณะที่เขากำลังมึนงงกับสถานการณ์ที่เกิดขึ้น จู่ๆ ก็มีหน้าต่างเกมปรากฎขึ้นมาพร้อมกับข้อความที่บอกว่า **หากเดบิวต์ไม่ได้ภายใน 365 วัน เขาจะต้องตาย!**',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/Debut_or_Die/542?tab=profile'},

    ]
    for item in id_rc_tt_dm:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Idol Drama
if ('Idol' in choices or 'Drama' in choices) and all(choice in ['Idol', 'Drama'] for choice in choices):
    id_dm = [
        {'image': 'manhwa_png/id_dm00.jpg',
         'caption': 'น้องเล็กพันธุ์ยักษ์',
         'markdown': 'ชื่ออังกฤษ : Giant Maknae\n\n'
         '**โลกที่สัตว์สามารถใช้ชีวิตเป็นมนุษย์ได้** สามารถทำงานได้หลากหลาย คนเหล่านั้นถูกเรียกว่า มนุษย์พันธุ์ใหม่\n\n'
         'แมริโกลด์ วงไอดอลที่ประกอบไปด้วยสมาชิกที่เป็นมนุษย์พันธุ์ใหม่ ทุกคนเป็นสัตว์พันธุ์เล็กกันหมด ยกเว้น**น้องใหม่ ยองอุน ที่ตัวสูงกว่าเมมเบอร์คนอื่นๆ ทุกคนคิดว่าเขาไม่มีทางเป็นสัตว์ตัวเล็กๆ ได้เลย**\n\n'
         'เกิดเป็นเรื่องราวการค้นหาตัวตนของน้องเล็กคนใหม่ พร้อมการไล่ตามความฝันในฐานะไอดอล',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/น้องเล็กพันธุ์ยักษ์/503?tab=episode'},

        {'image': 'manhwa_png/id_dm01.jpg',
         'caption': 'MAVE : สู่โลกอีกใบ',
         'markdown': 'ชื่ออังกฤษ : MAVE : Another World\n\n'
         '**อีเจน่า กำลังจะได้เดบิวต์เป็นไอดอล แต่กลับต้องมาฝันสลาย**เพราะมีคนทำให้ค่ายได้รับผลกระทบจนต้องออกจากค่าย อีเจน่ายังไม่ยอมละทิ้งความฝันจึงเตรียมตัวเพื่อเข้าแข่งขันในรายการเซอร์ไววัล\n\n'
         'วันหนึ่งเธอได้พบกับคนที่ทำให้ฝันเธอพังอย่าง จูชีอู เธอจึงตั้งใจว่าจะไม่ยุ่งด้วย แต่เธอได้รับข้อความพร้อมกับหน้าต่างภารกิจ **ถ้าอยากจะเป็นไอดอล ต้องร่วมมือกับจูชีอู**\n\n'
         'เรื่องราวของเหล่าไอดอลสาวที่มีพลังพิเศษ',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/MAVE_สู่โลกอีกใบ/504?tab=episode'},

    ]
    for item in id_dm:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])

# Idol Drama Time Travel
if ('Idol' in choices or 'Drama' in choices or 'Time Travel' in choices) and all(choice in ['Idol', 'Drama', 'Time Travel'] for choice in choices):
    id_dm_tt = [
        {'image': 'manhwa_png/id_dm_tt00.jpg',
         'caption': 'ขอลองสู้อีกครั้งนะ ไอดอล',
         'markdown': 'ชื่ออังกฤษ : Second Try Idol\n\n'
         '**ซอยอนอู เด็กฝึกค่าย YMM Entertainment ใช้เวลาฝึกนาน 10 ปี จนได้เป็นหนึ่งในทีมเดบิวต์ แต่เขากลับประสบอุบัติเหตุจนหน้าเสียโฉม** จึงเสียโอกาสนั้นไป\n\n'
         'เขาหันมาใช้ชีวิตในฐานะเทรนเนอร์ เด็กฝึกของเขาได้กลายเป็นไอดอลที่ประสบความสำเร็จมากที่สุดในเกาหลีใต้ ในระหว่างนั่งเครื่องบินเกิดเหตุไม่คาดคิดขึ้น เขาได้ย้อนเวลากลับมาก่อนที่ใบหน้าจะเสียโฉม\n\n'
         '**“ฉันได้รับโอกาสกลับมา คราวนี้จะไม่ให้มันจบลงแบบเดิมอีกแล้ว!”**',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/ขอลองสู้อีกครั้งนะ_ไอดอล/400?tab=episode'},

    ]
    for item in id_dm_tt:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])


# Idol Comedy
if ('Idol' in choices or 'Comedy' in choices) and all(choice in ['Idol', 'Comedy'] for choice in choices):
    id_cmd = [
        {'image': 'manhwa_png/id_cmd00.jpg',
         'caption': 'เดอะเฮฟเวินลีไอดอล',
         'markdown': 'ชื่ออังกฤษ : GThe Heavenly Idol\n\n'
         '**เรมบรารี มหาปุโรหิต ตื่นขึ้นมาอยู่ในร่างไอดอลเกาหลีคนหนึ่ง** หลังจากปะทะกับปีศาจที่ใครบางคนอัญเชิญมา\n\n'
         'เขาจะสามารถทำตัวกลมกลืนไปกับสภาพแวดล้อมที่ไม่คุ้นเคย และจะหาทางกลับไปยังโลกเดิมของตัวเองได้หรือไม่',
         'web':'Webtoon', 'link': 'https://www.webtoons.com/th/fantasy/the-heavenly-idol/list?title_no=5248'},

        {'image': 'manhwa_png/id_cmd01.jpg',
         'caption': 'พี่ชายของผมเท่ที่สุด',
         'markdown': 'ชื่ออังกฤษ : Hyung, You’re My Idol\n\n'
         '**ซูรยูยอจุน น้องเล็กของวงไอดอล** ได้รับของขวัญจากแฟนคลับเป็นแฟนฟิคที่มีเขาคู่กับเหล่าสมาชิกวง เมื่อได้ลองอ่านรยอจุนชอบ และจุดประกายการ**เริ่มเขียนแฟนฟิคของตัวเอง**\n\n'
         'วันหนึ่งสมาชิกของวงได้รู้ความลับของเขา รยอจุนจะทำอย่างไรต่อไป',
         'web':'KaKao Webtoon', 'link': 'https://th.kakaowebtoon.com/content/พี่ชายของผมเท่ที่สุด/72?tab=episode'},

    ]
    for item in id_cmd:
        st.image(item['image'], caption=item['caption'], width=200)
        st.markdown(item['markdown'])
        st.link_button(item['web'],item['link'])
