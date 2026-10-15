# Review xm2: menu3019, menu3021, menu3022, menu3024, menu3025, menu3027, menu3028, menu3029

Proposals: `rev_xm2.json` (121 rows). `check_fixes.py`: 0 proposed lines with errors. Every **ERRO** row of the 8 validation reports is covered.

## Screens

- **menu3019** (69 rows): encyclopedia descriptions (titles are menu3018#0-67; menu3019#15 is the post-Op08 version of #14, so 3018#i = 3019#i+1 from #15 on). Box 249 px, about 23 characters per line; the pane scrolls (menu3021#3 "Scroll"), but the validator keeps the Japanese line count, so most entries had to drop blank paragraph lines.
- **menu3021** (7 rows): encyclopedia list screen: help line, list title, column headers, intro text, header icon.
- **menu3022** (16 rows): series filter list for the encyclopedia (series titles), its title and help text.
- **menu3024** (2 rows): "change type" filter and its help text.
- **menu3025** (43 rows): unit names for the viewer list (menu3000 has the same names with ": Ground Only/Space Only").
- **menu3027** (4 rows): comm log (mail) list screen labels and intro text.
- **menu3028** (19 rows): mail list: sender (line 1) + preview of the letter (line 2, ends in "..."). The previews are now the first words of the new menu3029 letters.
- **menu3029** (19 rows): the letters (Barkholz x12, Nina x6, Marina x1).

## Fixes

ref | JP (short) | old EN (short) | new EN | reason
---|---|---|---|---
menu3019#0 | 旧ジオン公国軍の残党勢力。 / / 現在も、地球圏... | Remnant forces of the former Principa... | Remnants of the former / Principality of Zeon's / forces. They stil... (full in JSON) | width ERRO; re-wrapped to 5 lines, full meaning kept
menu3019#1 | エギーユ・デラーズを首長とする / 旧ジオン公国軍... | A remnant organization of the former ... | A remnant group of the / former Principality of / Zeon's forces, le... (full in JSON) | invented "hostility against the Earth Federation"; dropped GP02 theft + declaration of war; "Eguille" -> Aiguille; width
menu3019#2 | 月への移民の一部が設立した / 月面の帝国。 / ... | A lunar empire established by a porti... | A lunar empire founded / by some lunar / emigrants. / Under Marshal... (full in JSON) | invented "declared war against the Earth Federation"; dropped the "fighting ever since / stepped-up invasion of Earth" paragraph
menu3019#3 | オルファン内部に設立された / 研究団であり、 /... | A research group established inside O... | A research group formed / inside Orphan, and the / Orphan believers... (full in JSON) | dropped the whole combat-unit paragraph (Grand Cher, Antibody); "depart into the galaxy alongside Orphan" wrong (they raise Orphan out of the atmosphere); glossary ERRO
menu3019#4 | 近年、地球への襲撃を / 繰り返している正体不明の... | A mysterious fleet of unmanned weapon... | Unidentified unmanned / weapons that have often / raided Earth in r... (full in JSON) | invented "they wage war against Earth"; dropped why they got the name; Tulips -> Chulips (glossary)
menu3019#5 | 地球の手で、火星に追放された / 月移民の末裔。 ... | Descendants of lunar emigrants who we... | Descendants of lunar / emigrants whom Earth / exiled to Mars. / Lat... (full in JSON) | invented "autonomous nation" and "Jovian Union"; dropped ancient ruins, revenge, Gekiganger 3 as scripture and the full name of the Jovian Federation
menu3019#6 | 異世界バイストン・ウェルから / 地上へと追放され... | A private military force led by Drake... | A private army led by / Drake Luft, exiled from / the other world o... (full in JSON) | invented "superior military power"; dropped the Organic Machine / Orphan plot and the temporary Reclaimer alliance (glossary ERRO)
menu3019#7 | 外宇宙に存在する二重太陽系 / ペンタゴナワールド... | The governing organization that rules... | The governing power / that rules the Pentagona / World, a binary st... (full in JSON) | invented "five planets with an iron fist"; dropped Giwaza Lowau's Earth expedition (glossary ERRO)
menu3019#8 | ブルドリア太陽系の惑星グラドス / を中心とした軍... | A military state centered on the plan... | A military state centered / on the planet Grados in / the Burdoria ... (full in JSON) | dropped Le Cain / Admiral Gresco (glossary ERRO); width
menu3019#9 | 文化と呼ばれるものを持たず、 / 戦闘のみに特化さ... | A race of giant humanoids specialized... | A race of giants with / nothing called culture, / made solely for b... (full in JSON) | width; compacted, every clause kept
menu3019#10 | 女性のみで構成された、 / 巨人の戦闘種族。 / ... | A giant combat race composed solely o... | A warrior race of giants / made up only of women. / / They have bee... (full in JSON) | width (auto re-wrap would flatten the paragraphs)
menu3019#11 | ＵＣＥに在籍していた開発者。 / / その優れた能... | A developer formerly affiliated with ... | A former UCE developer. / With his exceptional / talent, he led a /... (full in JSON) | width; compacted, every clause kept
menu3019#12 | 各地に出没している正体不明機。 / / それぞれの... | An unidentified machine appearing in ... | An unidentified machine / appearing in various / places. / It acts ... (full in JSON) | width; compacted
menu3019#13 | 自己進化・自己再生・自己増殖の / 三大理論を元に... | The rampaging form of the Ultimate Gu... | The berserk form of the / "Ultimate Gundam," built / to renew Earth... (full in JSON) | one 60-word sentence, width ERRO; restructured
menu3019#14 | 地球圏の包括的統治と治安維持の / ために発足した... | The Earth Sphere governing organizati... | The Earth Sphere's / governing body, formed / to rule and secure it... (full in JSON) | width; "Allied Space Forces" -> UESF (連合宇宙軍 = United Earth Space Force)
menu3019#15 | 地球圏の包括的統治と治安維持の / ために発足した... | The Earth Sphere governing organizati... | The Earth Sphere's / governing body, formed / to rule and secure it... (full in JSON) | width; same as #14; "Gundam Prototype Unit 2" -> Gundam GP02 (glossary for ガンダム試作2号機)
menu3019#16 | ＵＣＥを構成する主要組織の / 一つで、ＵＣＥ内で... | One of the primary organizations comp... | One of the UCE's main / member organizations, / and the largest wit... (full in JSON) | width; compacted
menu3019#17 | 地球連合の主力の軍隊で、 / ＵＣＥを構成する /... | The main military force of the Earth ... | The main armed force of / the United Earth, and / one of the UCE's ... (full in JSON) | width; 地球連合 = "United Earth" to match United Earth Space Force (was "Earth Alliance")
menu3019#18 | ＵＣＥ所属の強襲揚陸艦。 / / ガンダム開発計画... | An assault landing craft belonging to... | A UCE assault landing / ship. / It serves as mothership / to the pr... (full in JSON) | "Eiphar Synapse" -> Eyphar Sinapus (glossary ERRO); "landing craft" -> assault landing ship
menu3019#19 | ＵＣＥ内の諜報機関。 / / 敵対組織の動向を調査... | An intelligence agency within the UCE... | An intelligence agency / within the UCE. / / It investigates and / ... (full in JSON) | width; compacted
menu3019#20 | ＵＣＥ独自の新型兵器開発部門。 / / ガンアーク... | The department responsible for develo... | The UCE's own / new-weapon development / division. Founded when / G... (full in JSON) | width; compacted
menu3019#21 | オルファンを浮上させようとする / リクレイマーに... | A warship organized to counter the Re... | A warship organized to / oppose the Reclaimers, / who seek to raise... (full in JSON) | "Brain Powered" -> Brain Powerd; width
menu3019#22 | ネルガル重工が、独自に建造した / 新鋭艦。 / ... | A cutting-edge battleship independent... | A cutting-edge ship built / independently by Nergal / Heavy Industr... (full in JSON) | width; both parenthetical glosses kept
menu3019#23 | ＵＣＥにより、建造された / 新造戦艦。 / / ... | A newly constructed battleship built ... | A new battleship built / by the UCE. / / It was made by refitting /... (full in JSON) | width; Fold -> fold (glossary); Attack Mode as in brief63019 fill
menu3019#24 | 異世界バイストン・ウェルから / 地上へと追放され... | A battleship exiled to the surface fr... | A battleship exiled from / the other world of / Byston Well to the ... (full in JSON) | width; "Ceila" -> Ciela; "Drake Forces" -> Drake Army (approved briefings)
menu3019#25 | ペンタゴナワールドでの / ポセイダルの統治に対す... | A resistance organization against Pos... | A resistance group / fighting Poseidal's rule / over the Pentagona ... (full in JSON) | re-wrap; compacted
menu3019#26 | 地球圏最大の民間企業。 / / 一般家電から軍需製... | The largest private corporation in th... | The largest private / company in the Earth / Sphere. A general make... (full in JSON) | width; "Mobile Suits" -> mobile suits (glossary)
menu3019#27 | アジア圏の企業グループ。 / / 古くから火星の開... | A corporate conglomerate based in the... | An Asian corporate / group. Deeply involved / in developing Mars fr... (full in JSON) | width; compacted
menu3019#28 | デラーズ・フリートの指導者。 / / 旧ジオン公国... | The leader of the Delaz Fleet. / / In... | Leader of the Delaz / Fleet. Carrying on the / former Principality ... (full in JSON) | width
menu3019#29 | シーマ艦隊司令官。 / / デラーズ・フリートの一... | Commander of the Cima Fleet. / / As a... | Commander of the Cima / Fleet. As part of the / Delaz Fleet, she fi... (full in JSON) | width; "Eguille" -> Aiguille Delaz
menu3019#30 | アナハイム・エレクトロニクスの / エンジニア。 ... | An engineer at Anaheim Electronics. /... | An engineer at Anaheim / Electronics. / / In charge of developing /... (full in JSON) | re-wrap; compacted
menu3019#31 | 地球連邦の宇宙軍の准将。 / / ガンダム開発計画... | A brigadier general in the Earth Fede... | An Earth Federation / space force Commodore. / As Gundam Developmen... (full in JSON) | "brigadier general" -> Commodore (准将); width
menu3019#32 | 連合宇宙軍提督。 / / ＵＣＥを統括するに当たり... | Admiral in the Allied Space Forces. /... | Admiral of the United / Earth Space Force. / Named its supreme / co... (full in JSON) | "Allied Space Forces" -> UESF; "upon unifying the UCE" misread (the UESF took charge of the UCE); width
menu3019#33 | 統一帝国ギガノスの元帥。 / / 強い選民思想を持... | Marshal of the United Empire of Gigan... | Marshal of the Unified / Empire of Giganos. A / staunch elitist, he... (full in JSON) | "United Empire" -> Unified Empire of Giganos (glossary); width
menu3019#34 | ギガノス軍中佐。 / / マスドライバーによる地球... | Lieutenant colonel in the Giganos mil... | A Giganos lieutenant / colonel. / He assassinated Marshal / Guiltor... (full in JSON) | width; Supreme Leader (brief63228 fill); Unified Empire
menu3019#35 | ＵＣＥ外務次官。 / / 各地の紛争調停のために、... | Vice Minister of Foreign Affairs for ... | UCE Vice Foreign / Minister. Heedless of / danger, she keeps up / p... (full in JSON) | "Cinq Kingdom" -> Sanc Kingdom; width
menu3019#36 | 異世界バイストン・ウェルから / 追放されたナの国... | Queen of the Kingdom of Na, exiled fr... | Queen of the Kingdom of / Na, exiled from the other / world of Byst... (full in JSON) | "Gran Garan" -> Gran-Garan (glossary ERRO); Drake Army; width
menu3019#37 | ポセイダル軍の近衛師団司令官。 / / ポセイダル... | Commander of the Royal Guard Division... | Commander of the / Poseidal Army's Imperial / Guard. Brainwashed an... (full in JSON) | width; Imperial Guard; no "his" for Poseidal (female per glossary)
menu3019#38 | エイジの姉。 / / グラドス人と地球人との融和を... | Older sister of Eiji. / / She advocat... | Eiji's older sister. / Urging harmony between / Grados and Earth pe... (full in JSON) | width; compacted
menu3019#39 | 戦艦マクロスの人気アイドル / 歌手。 / / 地... | Popular idol singer aboard the battle... | A popular idol singer on / the battleship Macross. / She debuted ab... (full in JSON) | width; compacted
menu3019#40 | ドモン・カッシュの兄。 / / 研究途中のデビルガ... | Older brother of Domon Kasshu. / / He... | Domon Kasshu's older / brother. / He stole the Devil / Gundam mid-r... (full in JSON) | 彼ら = Kyoji and the Devil Gundam ("of them", was "of him"); re-wrap
menu3019#41 | かつて、「ソロモンの悪夢」 / と呼ばれ恐れられた... | Ace pilot of former Zeon, once feared... | A former Zeon ace pilot / once feared as the / "Nightmare of Solomo... (full in JSON) | re-wrap; compacted
menu3019#42 | ミノフスキー粒子の出現により、 / 有視界戦闘が中... | Humanoid mobile weapons that appeared... | Humanoid mobile / weapons that became the / mainstay of close comba... (full in JSON) | width; compacted
menu3019#43 | ギガノスが開発した / 人型機動兵器。 / / 地... | Humanoid mobile weapons developed by ... | Humanoid mobile / weapons built by / Giganos. Via Dr. Lang / Plato,... (full in JSON) | width; compacted
menu3019#44 | オルファンの生み出す / オーガニック・プレートか... | Machines revived from Organic Plates ... | Machines born by / revival (rebirth) from the / Organic Plates that... (full in JSON) | "revival (rebirth)" restored; Grandchers -> Grand Chers, Brain Powereds -> Brain Powerds
menu3019#45 | ネルガル重工が開発した / 人型機動兵器。 / /... | Humanoid mobile weapons developed by ... | Humanoid mobile / weapons developed by / Nergal Heavy Industries. /... (full in JSON) | width; compacted
menu3019#46 | 異世界バイストン・ウェルで / 開発された、ダンバ... | Humanoid mobile weapons developed in ... | Humanoid mobile / weapons, the Dunbine / among them, made in the / ... (full in JSON) | width; compacted
menu3019#47 | ペンタゴナワールドで開発された / 人型機動兵器。... | Humanoid mobile weapons developed in ... | Humanoid mobile / weapons made in the / Pentagona World. They / fea... (full in JSON) | width; Class-A -> A-class
menu3019#48 | ３段可変機構を持つ / 人型機動兵器。 / / 戦... | Humanoid mobile weapons possessing a ... | Humanoid mobile / weapons with a / three-stage variable / mechanism... (full in JSON) | width; compacted
menu3019#49 | グラドス製の汎用人型機動兵器。 / / 様々な兵装... | General-purpose humanoid mobile weapo... | General-purpose / humanoid mobile / weapons made by / Grados. A bac... (full in JSON) | width; compacted
menu3019#50 | ガンダムファイト専用に / 開発された、ガンダムタ... | Gundam-type humanoid mobile weapons d... | Gundam-type humanoid / mobile weapons made / just for the Gundam / ... (full in JSON) | width; compacted
menu3019#51 | 紛争の再燃をきっかけに、 / 各地に出現している ... | A general term for special machines a... | The collective name for / the special machines / appearing in many ... (full in JSON) | width; compacted
menu3019#52 | ＵＣＥが、独自に開発した / 人型機動兵器。 / ... | Humanoid mobile weapons independently... | Humanoid mobile / weapons developed by / the UCE itself. / They wer... (full in JSON) | width; compacted
menu3019#53 | 海と大地の間に存在する異世界。 / / 地上界での... | An alternate world situated between t... | Another world that lies / between the sea and the / land. / It is s... (full in JSON) | "Gran Garan" -> Gran-Garan (glossary ERRO); invented "travelers"; Drake Army
menu3019#54 | 外宇宙に存在する５つの惑星の / 世界のこと。 /... | A realm consisting of five planets si... | A world of five planets / in outer space. / It is now ruled by a / ... (full in JSON) | width; compacted
menu3019#55 | レールガンの一種で、 / 隕石などの大質量の物体を... | A type of railgun equipped with the f... | A type of railgun, a / device that accelerates / and launches massi... (full in JSON) | re-wrap; compacted
menu3019#56 | 太平洋海溝で発見された / 超古代遺跡。 / / ... | A super-ancient relic discovered in t... | Super-ancient ruins / found in a Pacific Ocean / trench. / In truth... (full in JSON) | width; all four paragraphs kept
menu3019#57 | 木星蜥蜴が、 / 地球への侵攻の際に利用する、 /... | A form of instantaneous teleportation... | A kind of instant / teleportation based on / overtechnology, used b... (full in JSON) | width; compacted
menu3019#58 | 「機動戦艦ナデシコ」の / 劇中アニメーション。 ... | An anime within the series 'Mobile Ba... | A show within "Martian / Successor Nadesico." / A 39-episode anime ... (full in JSON) | "Mobile Battleship Nadesico" -> Martian Successor Nadesico (as menu3022#6); "Geki-Gangar" -> Gekiganger; "Jovian Union" -> Jovian Federation
menu3019#59 | 一年戦争時、ＵＣＥとジオン公国 / の間に締結され... | A wartime treaty concluded between th... | A wartime treaty signed / by the UCE and the / Principality of Zeon... (full in JSON) | width; compacted
menu3019#60 | 戦闘使役目的の / 巨人人型生物兵器ゼントラーディ... | The first intelligent lifeform in cos... | The first intelligent life / in cosmic history, / creator of the Ze... (full in JSON) | width; compacted
menu3019#61 | オルファンで発見されたプレート / に酷似したプレ... | Plates closely resembling the plates ... | A plate much like the / plates found in Orphan. / Its surface bears... (full in JSON) | width
menu3019#62 | デビルガンダムを構成する / アルティメット細胞が... | The evolved form of the Ultimate Cell... | The evolved form of the / Ultimate Cells that make / up the Devil G... (full in JSON) | re-wrap; compacted
menu3019#63 | 「一兵器としての機動性・汎用性 / を維持しつつ最... | A strategic support system of the UCE... | A UCE strategic support / system built on the / concept "a unit wit... (full in JSON) | width; compacted
menu3019#64 | 地球連邦政府が行った、 / 対外宇宙勢力用の防衛戦... | A defense force development project a... | An Earth Federation / Government project to / build defenses agains... (full in JSON) | width; compacted
menu3019#65 | 衛星ガーディアンの内部機関に / 搭載されているエ... | An energy substance mounted in the in... | An energy substance / inside the internal / engine of the satellite... (full in JSON) | width; compacted
menu3019#66 | 月の裏側に建設された、 / ギガノス軍の最終兵器。... | The ultimate weapon of the Giganos mi... | The Giganos military's / ultimate weapon, built / on the Moon's far... (full in JSON) | width; compacted
menu3019#67 | 量子力学における対生成の / 思想に基づき、 / ... | A hypothesized existence named under ... | A name based on pair / production in quantum / mechanics: the idea ... (full in JSON) | width; compacted
menu3019#68 | ＵＣＥの宇宙域における / 拠点の一つ。 / / ... | One of the UCE bases in space. / / Fo... | One of the UCE's bases / in space. / Once called Solomon, it / was ... (full in JSON) | re-wrap; "conquered Zeon forces" -> taken from the former Zeon; Federation faction (glossary)
menu3028#7 | バルクホルツ / 報告は聞いたよ。あれはマリナ君だ... | Barkholz / I heard the report. So tha... | Barkholz / I heard. ...So that was Marina... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#12 | バルクホルツ / 機は熟した。私はマリナ君とともに... | Barkholz / The time has come. I am go... | Barkholz / Time is ripe. I go with Marina... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#0 | バルクホルツ / タック君か？私だ。プライベート回... | Barkholz / Tak? It is me. Sending on ... | Barkholz / Tak? It's me. I'm sending this... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#1 | バルクホルツ / やあ。ガンアークの調子はどうかな... | Barkholz / Hello. How is the Gun Ark ... | Barkholz / Hello. How is the Gun Ark... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#2 | バルクホルツ / 君から連絡が来て驚いた。カーソン... | Barkholz / I was surprised to hear fr... | Barkholz / I was surprised to hear from... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#3 | バルクホルツ / やあ。まずは、無事でよかった。本... | Barkholz / Hello. First, glad you are... | Barkholz / Hello. First of all, I'm glad... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#4 | ニナ・パープルトン / はじめまして。って言うのは... | Nina Purpleton / Nice to meet you. Is... | Nina Purpleton / Nice to meet you. ...Is that a... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#5 | バルクホルツ / やあ。衛星の調査、ご苦労だったね... | Barkholz / Hello. Good work on the sa... | Barkholz / Hello. Good work on the satellite... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#6 | バルクホルツ / 久しぶり。作戦はうまくいったよう... | Barkholz / Long time no see. Operatio... | Barkholz / It's been a while. It seems the... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#8 | ニナ・パープルトン / お久しぶり。突然ごめんなさ... | Nina Purpleton / Long time no see. So... | Nina Purpleton / Long time no see. ...Sorry to... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#9 | バルクホルツ / まいったね。例の武装勢力アルバー... | Barkholz / Troublesome news. The arme... | Barkholz / Well, this is a fix. That armed... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#10 | バルクホルツ / 久しぶり。無事で帰ってきてくれて... | Barkholz / Long time no see. Glad you... | Barkholz / It's been a while. I'm glad you... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#11 | ニナ・パープルトン / 元気かしら。その後、何事も... | Nina Purpleton / How are you? Everyth... | Nina Purpleton / How are you? Nothing has... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#13 | ニナ・パープルトン / 報告は聞いたわ。こちらでも... | Nina Purpleton / I heard the report. ... | Nina Purpleton / I heard the report. On my end, I... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#14 | バルクホルツ / この通信記録は、全てが終わった後... | Barkholz / This log is set to send au... | Barkholz / This message has been set to... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#15 | ニナ・パープルトン / プリベンターが公開した資料... | Nina Purpleton / From Preventer files... | Nina Purpleton / From the materials the Preventer... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#16 | ニナ・パープルトン / 今、大丈夫？あなたに緊急で... | Nina Purpleton / Do you have a moment... | Nina Purpleton / Do you have a moment? There's... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#17 | ニナ・パープルトン / ＵＣＥ本部は、アークシリー... | Nina Purpleton / UCE HQ has officiall... | Nina Purpleton / It seems UCE HQ has officially... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3028#18 | マリナ・カーソン / タック。顔を合わせたら、言え... | Marina Carson / Tak. If we met, I cou... | Marina Carson / Tak. ...I don't think I could say... | preview = start of the new menu3029 letter; the auto re-wrap was merging the sender name into the preview line; #16/#17 width ERRO
menu3029#0 | タック君か？ / 私だ。 / プライベート回線で送... | Tak? / It is me. / I am sending this ... | Tak? It's me. I'm sending this / over a private line. / / ...I'm tr... (full in JSON) | after the first lines the EN was invented (explosion report, "despair", "mission to fulfill"); dropped the will, the hair ornament, the energy-core data
menu3029#1 | やあ。 / ガンアークの調子はどうかな。 / / ... | Hello there. / How is the Gun Ark per... | Hello. How is the Gun Ark / doing? / / Now that the energy core is ... (full in JSON) | from line 3 invented ("true specifications", combat data); dropped the additional function and the Albion/Marina paragraph
menu3029#2 | 君から連絡が来て驚いた。 / カーソン少尉が生きて... | I was surprised to hear from you. / S... | I was surprised to hear from you. / You say Ensign Carson might be ... (full in JSON) | invented "Buster Ark, correct?", "destroyed in testing", "misidentification"; dropped the pre-war UCE project / leak theory and Barkholz being questioned; Second Lieutenant -> Ensign
menu3029#3 | やあ。 / まずは、無事でよかった。 / / 本部... | Hello there. / First of all, I am gla... | Hello. First of all, I'm glad you're / safe. I just submitted a rep... (full in JSON) | invented "energy signature identical", "unmanned control unit"; dropped the whole Guardian System history, the city accident and "that is not Marina, she is dead"
menu3029#4 | はじめまして。 / …って言うのは、おかしいかしら... | Nice to meet you. / ...Does it sound ... | Nice to meet you. ...Is that a / strange thing to say? We've run / ... (full in JSON) | almost all invented (self-introduction, "exceptional pilot"); JP: Nina fixed Tak's botched data update and teases him about machines
menu3029#5 | やあ。 / 衛星の調査、ご苦労だったね。 / / ... | Hello there. / Thank you for your har... | Hello. Good work on the satellite / investigation. You've probably ... (full in JSON) | invented "core engine match", "I established the Design Bureau", "sister unit"; JP: unknown energy source, Rainen, satellites left in orbit, hundreds deployed
menu3029#6 | 久しぶり。 / 作戦はうまくいったようだね。 / ... | It has been a while. / It seems the o... | It's been a while. It seems the / operation went well. / / To think... (full in JSON) | dropped the old-documents paragraphs (Guardian's real output can move a colony; theoretical higher output)
menu3029#7 | 報告は聞いたよ。 / …あれはマリナ君だったんだね... | I heard the report. / ...So that real... | I heard the report. ...So that was / Marina, wasn't it? / / I didn'... (full in JSON) | meaning mostly right; stiff no-contraction voice, rewritten in Barkholz's warm voice
menu3029#8 | お久しぶり。 / …突然ごめんなさいね。 / / ... | It has been a while. / ...Pardon the ... | Long time no see. ...Sorry to / write out of the blue. / / I'm repa... (full in JSON) | meaning OK; voice and wrap
menu3029#9 | まいったね。例の武装勢力。 / アルバート・ライネ... | This is troublesome. That armed force... | Well, this is a fix. That armed / group. They say it's / Albert Rai... (full in JSON) | meaning mostly OK; voice; gender-neutral "their usual work"
menu3029#10 | 久しぶり。 / 無事で帰ってきてくれてよかった。 ... | It has been a while. / I am glad you ... | It's been a while. I'm glad you / came back safe. For a while I / w... (full in JSON) | meaning OK; "the Guardians" -> the Guardian; voice
menu3029#11 | 元気かしら。 / その後、何事もない？ / …だっ... | How are you doing? / Has everything b... | How are you? Nothing has / happened since then? ...If so, / good. /... (full in JSON) | width ERRO; voice
menu3029#13 | 報告は聞いたわ。 / こちらでも、先ほどガンアーク... | I heard the report. / I just finished... | I heard the report. On my end, I / just managed to analyze the / Gu... (full in JSON) | "parts that have not finished analyzing" ungrammatical; バルクホルツさん -> Mr. Barkholz
menu3029#14 | この通信記録は、全てが終わった後に / 自動的に君... | This communication log is set to be t... | This message has been set to / reach you automatically after / ever... (full in JSON) | width ERRO; "My cause, and Marina's cause" -> Marina's and my great cause
menu3029#15 | プリベンターが公開した資料から、 / ガーディアン... | From the materials released by the Pr... | From the materials the Preventer / released, the truth about the / ... (full in JSON) | hedges (でしょう, みたい) restored
menu3029#16 | 今、大丈夫？ / あなたに緊急で伝えたいことがあっ... | Do you have a moment right now? / The... | Do you have a moment? There's / something urgent I need to tell / y... (full in JSON) | "That is your machine" over-specified その機体; hedges kept
menu3029#17 | ＵＣＥ本部は、アークシリーズと / ガーディアンを... | UCE headquarters seems to have offici... | It seems UCE HQ has officially / decided to scrap the Ark Series / ... (full in JSON) | Second Lieutenant -> Ensign Carson (少尉); でしょう restored
menu3029#18 | タック。 / …顔を合わせたら、言えないだろうから... | Tak. / ...Face-to-face, I could not s... | Tak. ...I don't think I could say / this face to face... so I'll ju... (full in JSON) | "...I promise" -> "...It's a promise." (約束よ); first lines restructured
menu3029#12 | 機は熟した。 / 私はマリナ君とともに行く。 / ... | The time has come. / I am going with ... | The time is ripe. / I go with Marina. / / ...Farewell. (full in JSON) | 機は熟した = "The time is ripe"; needed so preview 3028#12 can carry "Marina"
menu3021#3 | スクロール：㊤㊦ 戻る：× | Scroll: ㊤㊦ Back: × | Scroll: ㊤㊦ Back: × | ideographic space between the two items, as in the JP (was one ASCII space)
menu3021#8 | ここではキャンペーン中に登場した / 各種用語の説... | Here, you can refer to explanations /... | Here you can view descriptions / of terms seen in the Campaign. | width ERRO
menu3022#5 | ブレンパワード | Brain Powered | Brain Powerd | "Brain Powered" -> Brain Powerd (official title / glossary)
menu3022#7 | 新機動戦記ガンダムＷ Ｅｎｄｌｅｓｓ Ｗａｌｔｚ | Mobile Suit Gundam Wing: Endless Waltz | Gundam Wing: Endless Waltz | width ERRO 405 > 400: short form of the title
menu3022#8 | 機動戦士ガンダム 逆襲のシャア | Mobile Suit Gundam: Char's Counterattack | Gundam: Char's Counterattack | width ERRO 415 > 400: short form of the title
menu3022#9 | 機動戦士ガンダム００８３ ＳＴＡＲＤＵＳＴ ＭＥＭＯＲＹ | Mobile Suit Gundam 0083: Stardust Memory | Gundam 0083: Stardust Memory | width ERRO 428 > 400: short form of the title
menu3022#10 | 超時空要塞マクロス / 超時空要塞マクロス 愛・お... | The Super Dimension Fortress Macross ... | Super Dimension Fortress Macross / Macross: Do You Remember Love? | official title has no "The"
menu3024#1 | 選んだタイプに変更します | Changes to selected type | Switch to this type | width ERRO 242 > 208
menu3025#2 | ガンダム試作１号機 | Gundam Prototype Unit 1 | Gundam GP01 | Gundam Prototype Unit 1 -> Gundam GP01 (glossary, menu3000)
menu3025#3 | ガンダム試作１号機Ｆｂ | Gundam Prototype Unit 1 Fb | Gundam GP01-Fb | -> Gundam GP01-Fb (menu3000)
menu3025#5 | ガンダム試作３号機 | Gundam Prototype Unit 3 | Gundam GP03 | -> Gundam GP03 (glossary; auto row menu3025#6 = "Gundam GP03 (Stamen)")
menu3025#100 | ガンアーク（タック機） | Gun Ark (Tak Custom) | Gun Ark (Tak) | "(Tak Custom)" implies a custom variant; タック機 = Tak's machine; menu3000#88 "Gun Ark (Tak)"
menu3025#101 | ガンアーク（タック機） 戦闘機形態 | Gun Ark (Tak Custom) Fighter | Gun Ark (Tak) Fighter | same as #100
menu3027#8 | ここでは他の人物から送られてくる / 通信メールを... | Here you can view incoming communicat... | Here you can read the mail / other people send you. | width ERRO 487 > 279

## Recurring labels (JP -> EN)

JP | EN | Source / note
---|---|---
戻る：× | Back: × | auto tm (menu3021#2, menu3027#2), hud3013
決定：○ | OK: ○ | common.json#7 (approved)
選択：㊤㊦ | Select: ㊤㊦ | hud3013 (approved)
スクロール：㊤㊦　戻る：× | Scroll: ㊤㊦　Back: × | menu3021#3 (ideographic space as in the JP); menu3027#3 copies it
選択：㊤㊦　決定：○　戻る：× | Select: ㊤㊦　OK: ○　Back: × | menu3013#0 (other reviewer): the return has "Confirm" and two ASCII spaces; should follow common.json "OK" and the ideographic space
事典 / ㌔事典 | Encyclopedia / ㌔Encyclopedia | menu3004#9 (repeat into menu3021#0)
通信ログ / ㌔通信ログ | Comm Log / ㌔Comm Log | menu3004#10 (repeat into menu3027#0)
事典リスト / 通信ログリスト | Encyclopedia List / Comm Log List |
ＳＴＡＴＥ / ＷＯＲＤ / ＣＯＮＴＥＮＴＳ / ＲＥＣＯＲＤ　ＩＤ | STATE / WORD / CONTENTS / RECORD ID | kept in capitals like the JP
タイトルリスト / タイプ変更 | Title List / Change Type |
選んだ～に変更します | Filter list by selected title / Switch to this type | 208 px box for menu3024
バルクホルツ / ニナ・パープルトン / マリナ・カーソン | Barkholz / Nina Purpleton / Marina Carson | senders in menu3028 (menu3014 full names)
ドレイク軍 | Drake Army | approved briefings (brief63016, 63103, 63233, 63256); the menu3018#6 return has "Drake Forces"
連合宇宙軍 | United Earth Space Force / UESF | glossary (returns had "Allied Space Forces")
木連 | Jovian Federation (Jovians) | glossary (returns had "Jovian Union")
ガンダム２号機 / ガンダム試作２号機 | Gundam Unit 2 / Gundam GP02 | brief63171 fill "Gundam Unit 1"; glossary GP02
外務次官 | Vice Foreign Minister | brief63227 fill
総帥 | Supreme Leader | brief63228 fill
強攻型 | Attack Mode | brief63019 fill
人型機動兵器 | humanoid mobile weapon(s) | used for every mecha class in menu3019#42-52

## Doubts left for the owner (not changed or decided provisionally)

1. **Line budget of the encyclopedia.** The pane scrolls, but max_lines = the Japanese line count. Fitting a full translation at about 23 characters per line forced me to drop most blank paragraph lines and to run paragraphs together in 31 entries (#0, #1, #4, #6, #8, #11, #14, #15, #18, #20, #22, #24-29, #32, #33, #35, #37, #42, #43, #45-47, #49, #52, #57, #65, #66); 25 more lost all their blank lines. The style is compact, but no sentence is dropped. If the box can hold more lines, it is better to measure it and raise max_lines; then I can restore the blank lines and the fuller phrasings (for example #14/#15 "UESF and U.N." are abbreviations because of space).
2. **menu3019#7 オルダナ・ポセイダル** (Oldana): the game text has a spelling different from glossary オルドナ (Oldna). I wrote "Oldna Poseidal" (glossary); probably a typo in the original.
3. **menu3019#8 ブルドリア太陽系**: no glossary entry; transliterated "Burdoria system" (the return had "Bourdelia"). It needs a Layzner source.
4. **menu3019#17 地球連合**: no glossary entry. I used "United Earth" so it matches 連合宇宙軍 = United Earth Space Force; the return had "Earth Alliance".
5. **menu3019#23 強攻型**: "Attack Mode" follows the brief63019 fill; Macross sources often say "Storm Attack mode".
6. **menu3022#7-9 series titles**: the full official titles do not fit 400 px (405/415/428). I used "Gundam Wing: Endless Waltz", "Gundam: Char's Counterattack", "Gundam 0083: Stardust Memory". "Mobile Suit Gundam Wing Endless Waltz" (no colon) would be exactly 400 px. menu3072#72-74/78 are auto copies of these rows. menu3022#1 "Aura Battler Dunbine" (official English title) is kept even though the glossary warns 聖戦士 = Holy Warrior.
7. **menu3028 previews** were rebuilt automatically as the start of each new letter. #7 ("I heard. ...So that was Marina...") and #12 ("Time is ripe. I go with Marina...") are abridged so that the required name "Marina" fits in 340 px. #2 keeps a glossary warning (少尉/Ensign is not in the preview). If the 3029 wording changes, the previews must be regenerated.
8. **Voice of the letters**: I used contractions and the warm, paternal tone the INDICE asks for Barkholz (the return had stiff, uncontracted English). His 私->僕 slips (#2, #7, #9) have no English equivalent. #12 and #14 keep the spoilers exactly as written. In #14, "残念だが、君たちが勝った" is rendered "I'm sorry to say it means you won".
9. **バルクホルツさん (Nina, #4/#13)** = "Mr. Barkholz", and バルクホルツ博士 (#15/#17) = "Dr. Barkholz". Tell me if you prefer "Dr." throughout.
10. **menu3029#16 その機体 / あの機体**: I kept it neutral ("the machine" / "that machine"). The return had "your machine", which assumes it is Tak's Gun Ark.
11. **menu3025 names** were aligned with the menu3000 return (GP01, GP01-Fb, GP03, "Gun Ark (Tak)"); that table is reviewed in parallel, so the two must agree. Also, the glossary's "Aestivalis (Akito C.)" for エステバリス(アキト専用機) looks like a typo; menu3025#49 keeps "Aestivalis (Akito Custom)".
12. **Encyclopedia titles (menu3018, another reviewer)**: they must match these texts: 木連 = Jovian Federation (the return has "Jovian Union"), ゲキ・ガンガー３ = Gekiganger 3 ("Geki-Gangar 3"), 連合宇宙軍 = United Earth Space Force ("Allied Space Forces"), コンペイトウ = Konpei Island ("Confeito"), ドレイク軍 = Drake Army, 機動戦艦ナデシコ = Nadesico.
13. BASE_RULES.md is not available on this machine; I followed PLANO.md and the rules in the task.

