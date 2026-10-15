# Glossário (ACE2)

Gerado por `tools/ace2/agent_docs.py` a partir de `work/glossary/` (fonte da verdade: `names.json`). Só aparecem nomes que existem no texto do jogo; "ocorr." é quantas vezes o japonês aparece.

- **Obrigatório:** todo nome desta página que aparece no japonês de uma linha deve aparecer em inglês exatamente assim. O validador rejeita a linha se o nome de personagem, unidade, nave, facção ou lugar faltar.
- Na fala, use a forma curta quando o japonês usa a forma curta (ex.: シナプス → Sinapus).
- **Gênero:** use a coluna; quando ela estiver vazia, não deduza pelo nome.
- Nome que não está aqui nem no `glossary` do lote: translitere, marque em `notes` e proponha em `report.glossary_proposals` com a fonte (título da página na wiki da série).

## Grafias fixadas pelo projeto (não "corrija")

| Use | Nunca | Por quê |
|---|---|---|
| Lt. | Lt. JG  | rank ladder 少尉 Ensign / 中尉 Lieutenant / 大尉 Captain (Kou = Ensign, Burning = Captain on the Gundam Wiki) |
| Lieutenant | Lieutenant JG | same ladder |
| Captain South Burning | Lieutenant South Burning | Gundam Wiki: South Burning, Captain (大尉) |
| Captain Burning | Lieutenant Burning | same |
| Capt. Burning | Lt. Burning | same |
| Major Anavel Gato | Lt. Commander Anavel Gato | Gundam Wiki: Anavel Gato, Major (少佐) |
| Cowen | Kowen | Gundam Wiki page title John Cowen (Kowen redirects); in-game rank 准将 = Commodore |
| Tak | Tack | SRW wiki / research macross_ace_original.json: Tak Kepford (owner decision pending) |
| Sinapus | Synapse | Gundam Wiki page title Eyphar Sinapus (owner decision pending; Synapse is the common form) |
| Barkholz | Barkholtz | research macross_ace_original.json (no wiki page; owner decision pending) |
| Giganos | Gigano | Dragonar wiki page title Giganos |

## Tratamentos e termos recorrentes (como na Operação 01)

| Japonês | Inglês | Nota |
|---|---|---|
| 少尉 | Ensign |  |
| 中尉 | Lieutenant (Lt.) |  |
| 大尉 | Captain (Capt.) | army/MS rank; a ship's captain (艦長) is also Captain |
| 少佐 | Major |  |
| 准将 | Commodore |  |
| 提督 | Admiral |  |
| 艦長 | Captain |  |
| 研究主任 | Chief Researcher |  |
| ＵＣＥ | UCE |  |
| 地球連邦 | Earth Federation |  |
| 連邦派 | Federation faction |  |
| ジオン残党 | Zeon remnants |  |
| プリベンター | Preventer |  |
| トリントン基地 | Torrington Base |  |
| 強襲揚陸艦 | assault landing ship |  |
| モビルスーツ | mobile suit |  |
| メタルアーマー | Metal Armor |  |
| ミノフスキー粒子 | Minovsky particles |  |
| メインウェポン | main weapon |  |
| サブウェポン | sub-weapon |  |
| 新型機 | new unit |  |
| 機体 | unit / machine | Op 01 uses 'unit' for mecha in general, 'machine' when the speaker is the developer |
| オペレーション | Operation |  |
| 二階級特進 | promoted two ranks |  |

## Retratos do briefing (`<op(N,1)>`)

| N | Quem fala | Gênero | Papel | Confiança |
|---|---|---|---|---|
| 31 | Irene Carrier | female | acting captain of the Novis Noa | high |
| 32 | Yurika Misumaru | female | captain of the Nadesico | high |
| 33 | Kouichiro Misumaru | male | UCE Space Force admiral (Yurika's father) | high |
| 34 | Ruri Hoshino | female | Nadesico operator | high |
| 36 | Lucrezia Noin | female | tactical staff officer (特尉, Special Lieutenant) from the Preventer | high |
| 37 | Eyphar Sinapus | male | captain of the Albion | high |
| 38 | South Burning | male | Captain, mobile weapons unit commander at Torrington | high |
| 39 | John Cowen | male | Commodore | high |
| 40 | Misa Hayase | female | Macross bridge officer (callsign Delta 1) | high |
| 41 | Bruno J. Global | male | captain of the Macross | high |
| 43 | Tak Kepford | male | Gun Ark pilot (protagonist) | medium |
| 44 | Marina Carson | female | Tak's partner; declared killed in Op 01, later the pilot of the Buster Ark | high |
| 45 | Daba Myroad | male | rebel leader, L-Gaim pilot | high |
| 46 | Amuro Ray | male | Captain, field commander of the Albion's mobile suit team | medium |
| 49 | Nina Purpleton | female | Anaheim Electronics engineer (Gundam GP01/GP03) | high |
| 50 | Fidel Barkholz | male | Chief Researcher, head of Gun Ark development | high |
| 54 | Ciela Lapana | female | Queen of Na | high |
| 55 | Albion bridge operator | None | bridge operator; gender unknown, keep neutral | medium |
| 56 | Linda Plato | female | Dragonar transport unit | high |

Retratos que não estão na tabela: descubra pelo contexto e informe em `report.portrait_speakers`.

## Personagens

### Mobile Suit Gundam 0083: Stardust Memory

| Japonês | Inglês | Forma curta | Gênero | Papel | Personalidade (voz) | Ocorr. |
|---|---|---|---|---|---|---|
| ニナ・パープルトン | Nina Purpleton | ニナ = Nina | female | Anaheim Electronics systems engineer on the Gundam Development Project, assigned to the Albion with GP01; G... | Talented and obsessively devoted to her Gundams; annoyed by Kou's childishness at first... | 10 |
| アナベル・ガトー | Anavel Gato | ガトー = Gato | male | Main antagonist of 0083; Zeon ace "Nightmare of Solomon", Delaz Fleet pilot who steals Gundam GP02 and late... | Honorable, idealistic career soldier; charismatic leader who fights on the front line;... | 6 |
| エギーユ・デラーズ | Aiguille Delaz | デラーズ = Delaz | male | Leader of the Delaz Fleet and mastermind of Operation Stardust; former Zeon colonel loyal to Gihren Zabi. W... | Zealous idealist devoted to Spacenoid independence and Gihren's cause; stern but patern... | 6 |
| シーマ・ガラハウ | Cima Garahau | シーマ = Cima | female | Commander of the Cima Fleet (ex-Zeon marines); allied with the Delaz Fleet, then betrays it to the Federati... | Scheming, harsh and venomous, intolerant of failure, yet decisive and fiercely loyal to... | 4 |
| エイパー・シナプス | Eyphar Sinapus | シナプス = Sinapus | male | Earth Federation captain (Captain, 大佐) of the assault carrier Albion; leads the pursuit of the stolen GP02. | Grizzled veteran with a commanding presence and keen tactical mind; relies on his own j... | 3 |
| サウス・バニング | South Burning | バニング = Burning | male | Veteran Earth Federation pilot (Captain, 大尉), leader of the Burning Team on the Albion and Kou's mentor; KI... | Experienced, strict but fatherly mentor to the young pilots. (The wiki personality sect... | 3 |
| コウ・ウラキ | Kou Uraki | コウ = Kou | male | Protagonist of 0083; 19-year-old Earth Federation test pilot from Torrington Base assigned to the Albion; p... | Hot-tempered and rash, often questions orders; mobile suit otaku; fiercely protective o... | 2 |
| ジョン・コーウェン | John Cowen | コーウェン = Cowen | male | Earth Federation Vice Admiral (中将), commander of the 3rd Earth Orbital Fleet and head of the Gundam Develop... | Reform-minded, determined officer who does everything he can against Operation Stardust... | 2 |
| ジャクリーヌ・シモン | Jacqueline Simone | シモン = Simone | female | Albion bridge operator (radar/sensors, port side), Warrant Officer; later assigned to the Titans. | Minor bridge crew character; the wiki gives no personality information. | 1 |
| ピーター・スコット | Peter Scott | スコット = Scott | male | Albion bridge radar operator, Warrant Officer; later Titans. | Least experienced of the bridge crew; very conscientious and dutiful. | 1 |

### Mobile Suit Gundam: Char's Counterattack

| Japonês | Inglês | Forma curta | Gênero | Papel | Personalidade (voz) | Ocorr. |
|---|---|---|---|---|---|---|
| アムロ・レイ | Amuro Ray | アムロ = Amuro | male | Earth Federation ace Newtype pilot; in CCA a Londo Bell mobile suit team leader (Captain) aboard the Ra Cai... | Withdrawn, machine-obsessed teen in the original series; by CCA a mature, dependable ve... | 5 |
| シャア・アズナブル | Char Aznable | シャア = Char | male | "Red Comet"; in CCA the supreme leader of Neo Zeon who plans to drop Axis on Earth; pilots the Sazabi from... | Charismatic, highly respected leader with a cold, ruthless side; mentally fragile, burd... | 1 |
| ブライト・ノア | Bright Noa |  | male | Londo Bell task force commander, captain of the Ra Cailum (rank: Captain) | loyal, strict disciplinarian, strong leader | 1 |

### Mobile Fighter G Gundam

| Japonês | Inglês | Forma curta | Gênero | Papel | Personalidade (voz) | Ocorr. |
|---|---|---|---|---|---|---|
| ドモン・カッシュ | Domon Kasshu | ドモン = Domon | male | Neo Japan Gundam Fighter (Shining Gundam, then God Gundam); King of Hearts and leader of the Shuffle Alliance | Hot-blooded, brash, impulsive and impatient; socially awkward, but has a strong sense o... | 10 |
| キョウジ・カッシュ | Kyoji Kasshu | キョウジ = Kyoji | male | Domon's older brother and a Neo Japan scientist; co-developer of the Ultimate Gundam, later the Devil Gunda... | Kind and gentle; loves his younger brother and taught him to have faith in others. | 5 |
| ライゾウ・カッシュ | Raizo Kasshu | ライゾウ = Raizo | male | Neo Japan scientist; father of Domon and Kyoji, co-creator of the Ultimate Gundam. |  | 1 |
| 東方不敗 | Master Asia |  | male | Neo Hong Kong Gundam Fighter, Domon's martial-arts master, former King of Hearts | stoic, strict, secretly compassionate | 1 |

### Mobile Suit Gundam Wing / Endless Waltz

| Japonês | Inglês | Forma curta | Gênero | Papel | Personalidade (voz) | Ocorr. |
|---|---|---|---|---|---|---|
| ゼクス・マーキス | Zechs Merquise | ゼクス = Zechs | male | Ace pilot (Tallgeese, Tallgeese III); former OZ officer and White Fang leader; Preventer agent ('Preventer... | Proud, chivalrous and self-loathing; a brilliant pilot torn between knightly ideals and... | 2 |
| リリーナ・ドーリアン | Relena Darlian | リリーナ = Relena | female | Female lead; heir of the Sanc Kingdom (real name Relena Peacecraft), Zechs's younger sister, and a pacifist... | Idealistic, determined pacifist; dignified and unafraid to confront soldiers. | 2 |
| ルクレツィア・ノイン | Lucrezia Noin | ノイン = Noin | female | Mobile suit pilot and former OZ Specials instructor; Preventer agent ('Preventer Fire'); Zechs's devoted pa... | Mature, composed, slightly tomboyish; an idealist who dislikes war, but fights hard for... | 2 |
| アルトロン | Altron | (forma curta) |  | Wufei's upgraded Gundam (XXXG-01S2); the same machine ACE2 calls Gundam Nataku |  | 2 |
| エイサップ鈴木 | Asap Suzuki | エイサップ = Asap | male | Protagonist; young man of mixed Japanese-American heritage pulled into Byston Well, where he becomes a Holy... | Earnest and idealistic, but angry about his place between two countries. Grows into a d... | 1 |
| カトル・ラバーバ・ウィナー | Quatre Raberba Winner | カトル = Quatre | male | Gundam pilot (Gundam Sandrock); heir of the wealthy Winner family of the L4 colonies; commands the Maganac... | Kind, polite, empathetic pacifist and a reluctant soldier. Uses the soft first-person p... | 1 |
| サコミズ・シンジロウ | Shinjiro Sakomizu | サコミズ = Sakomizu | male | Antagonist; former WWII Imperial Japanese Ohka (kamikaze) pilot who became King of the Hojo Kingdom in Byst... | Proud, imperious old king haunted by wartime Japan. Charismatic and bitter, set on retu... | 1 |
| デュオ・マックスウェル | Duo Maxwell | デュオ = Duo | male | Gundam pilot (Gundam Deathscythe Hell); calls himself the God of Death | Cheerful, talkative, jokey and casual; says he 'runs and hides but never lies'. Fierce... | 1 |
| トロワ・バートン | Trowa Barton | トロワ = Trowa | male | Gundam pilot (Gundam Heavyarms); mercenary and circus clown | Quiet, calm and emotionally reserved; speaks little and is loyal to his comrades, espec... | 1 |
| ヒイロ・ユイ | Heero Yuy | ヒイロ = Heero | male | Gundam pilot (Wing Gundam Zero); Preventer agent in the Endless Waltz era | Stoic, terse 'perfect soldier'; cold on the surface, ruthless on missions, protective o... | 1 |
| プリベンター・ウインド | Preventer Wind |  | male | Zechs Merquise's Preventer codename. |  | 1 |
| レディ・アン | Lady Une |  | female | Treize Khushrenada's aide and OZ Space Force commander (Second-Class Special Colonel); after the war, leade... | Split personality: a cold, ruthless military persona and a gentle, pacifist persona tha... | 1 |
| 張五飛 | Chang Wufei | 五飛 = Wufei | male | Gundam pilot (Shenlong/Altron, called Nataku); sides with the Mariemaia Army in Endless Waltz and in ACE2's... | Proud and honor-obsessed; obsessed with justice; despises weakness; prone to angry outb... | 1 |

### Super Dimension Fortress Macross: Do You Remember Love?

| Japonês | Inglês | Forma curta | Gênero | Papel | Personalidade (voz) | Ocorr. |
|---|---|---|---|---|---|---|
| リン・ミンメイ | Lynn Minmay | ミンメイ = Minmay | female | Idol singer aboard the Macross; her songs (culture) are the key to defeating the Zentradi. | Bright, cheerful and ambitious pop idol, somewhat self-absorbed; infatuated with Hikaru. | 5 |
| エキセドル4970 | Exsedol 4970 | エキセドル = Exsedol | male | Zentradi chief archivist / adviser serving under Vrlitwhai. | Analytical, logical and encyclopedic; deeply curious about (and baffled by) human culture. | 3 |
| キム | Kim |  | female | SDF-1 Macross bridge operator (one of the three bridge operators with Vanessa and Shammy). | Boyish, forward and gossipy; teases the younger Shammy. | 3 |
| ブリタイ7018 | Vrlitwhai 7018 | ブリタイ = Vrlitwhai | male | Zentradi fleet commander under the Boddole Zer Main Fleet; pursues and later allies with the Macross. | Massive, tenacious, honorable veteran warrior; pragmatic enough to cooperate with the h... | 3 |
| 一条輝 | Hikaru Ichijyo | 輝 = Hikaru | male | Protagonist of Macross DYRL; former civilian stunt flyer turned U.N. Spacy VF-1 Valkyrie pilot (Skull Squad... | Hot-headed, impulsive and stubborn young pilot who grows into responsibility; caught in... | 3 |
| 早瀬未沙 | Misa Hayase | 未沙 = Misa | female | U.N. Spacy officer (Lieutenant), bridge officer/coordinator of the SDF-1 Macross. | Stern, by-the-book, duty-bound officer with little humor at work; softens and grows clo... | 3 |
| ブルーノ・J・グローバル | Bruno J. Global | グローバル = Global | male | Captain of the SDF-1 Macross (U.N. Spacy). | Calm, old-fashioned veteran commander with a broad strategic view; pipe smoker who disl... | 2 |
| ミリア639 | Milia 639 |  | female | Same character as Milia Farina Jenius; her DYRL-era Meltran designation before joining the humans. | Proud, combative Meltran ace. | 2 |
| ゴルグ・ボドルザー | Golg Boddole Zer | ボドルザー = Boddole Zer | male | Supreme commander of the Zentradi main fleet. |  | 1 |
| ゴル・ボドルザー | Golg Boddole Zer | ボドルザー = Boddole Zer | male | Supreme commander of the Zentradi main fleet; main antagonist of DYRL. | Ancient, imposing and absolute; views culture as contamination to be wiped out. | 1 |
| マクシミリアン・ジーナス | Maximilian Jenius | マックス = Max | male | U.N. Spacy ace VF-1 pilot, Hikaru's wingman in Skull Squadron. | Calm, cheerful, unflappable prodigy pilot; later falls for and marries the Meltran ace... | 1 |
| ミリア・ファリーナ・ジーナス | Milia Fallyna Jenius | ミリア = Milia | female | Meltrandi (female Zentradi) ace pilot of the Queadluun-Rau; rival and later wife of Max. | Proud, fiercely competitive warrior obsessed with being the best; falls for Max after h... | 1 |
| ロイ・フォッカー | Roy Focker | フォッカー = Focker | male | Skull Squadron leader, veteran ace VF-1S pilot and Hikaru's senpai/mentor. | Brave, easygoing 'man's man' and ladies' man; rough exterior hiding compassion and humo... | 1 |

### Aura Battler Dunbine / The Wings of Rean

| Japonês | Inglês | Forma curta | Gênero | Papel | Personalidade (voz) | Ocorr. |
|---|---|---|---|---|---|---|
| ショウ・ザマ | Show Zama | ショウ = Show | male | Protagonist; Holy Warrior (Seisenshi) from Tokyo summoned to Byston Well; defects from Drake Luft to the re... | Hot-blooded, stubborn young motocross racer who grows into a serious, driven warrior. H... | 13 |
| シーラ・ラパーナ | Ciela Lapana | シーラ = Ciela | female | Queen of the Kingdom of Na; commands the aura battleship Gran-Garan; gives Sho the Billbine | Serene, dignified young queen with strong Aura Power and a sense of duty to all of Byst... | 13 |
| 黒騎士 | Black Knight |  | male | Masked identity of Burn Bunnings, Drake's former commander, after Sho defeats him; Sho's rival; pilots Zwar... | Once proud and respected, now bitter and obsessed with revenge on Sho. Cold, theatrical... | 6 |
| ジェリル・クチビ | Jeryll Coochibie | ジェリル = Jeryll | female | Holy Warrior from the second group summoned by Drake (said to be from Dublin, Ireland); enemy ace who pilot... | Violent, impulsive and bloodthirsty; enjoys destruction. Her enormous, unstable Aura Po... | 2 |
| ジャコバ・アオン | Jacoba Aon |  | female | Queen of the Ferario, who lives in the Land of Water. Late in the series she sends every Aura Machine and i... | Aloof and self-centred; puts her own race and Byston Well first and does not care what... | 2 |
| ドレイク・ルフト | Drake Luft | ドレイク = Drake | male | Main antagonist; Lord of House Luft in the Kingdom of Ah (アの国), who summons Holy Warriors and wages war to... | Ambitious, scheming warlord who believes his conquest is justified. Loves his daughter... | 2 |
| マーベル・フローズン | Marvel Frozen | マーベル = Marvel | female | Holy Warrior from a ranching family near Dallas, Texas; resistance pilot (House Givun); pilots Dunbine in ACE2 | Confident, kind and level-headed. A skilled pilot who first meets Sho as an enemy and t... | 2 |
| ガラリア・ニャムヒー | Garalia Nyamhee | ガラリア = Garalia | female | Knight in Burn's squadron of Drake's army; pilots Drumlo, Virunvee and Bastole | Fiercely ambitious and hot-tempered. Desperate to win glory and restore her family name... | 1 |
| チャム・ファウ | Cham Huau | チャム = Cham | female | Mi Ferario (fairy) companion of Sho | Tiny, noisy and emotional; Sho's cheerleader. She sides with him loudly against enemies... | 1 |
| トッド・ギネス | Todd Guinness | トッド = Todd | male | American Holy Warrior summoned with Sho; fights for Drake and later Bishot Hate; pilots Wryneck in ACE2 | Brash and proud. At first he treats Byston Well as a game, then becomes obsessed with b... | 1 |
| バーン・バニングス | Burn Bunnings | バーン = Burn | male | Drake Luft's knight commander and Show Zama's former superior and rival; later fights masked as the Black K... | Proud and capable commander respected by his men; grows obsessed with defeating Show af... | 1 |
| リリス・ファウ | Lilith Fau | リリス = Lilith | female | Last surviving fairy (Mirauli) of the Pentagona World; companion to Daba Myroad | Cheerful, chatty little fairy who loves Daba's group. No use in a fight, but a good coo... | 1 |

### Heavy Metal L-Gaim

| Japonês | Inglês | Forma curta | Gênero | Papel | Personalidade (voz) | Ocorr. |
|---|---|---|---|---|---|---|
| クワサン・オリビー | Quwasan Olibee | クワサン = Quwasan | female | Daba's adopted younger sister and fiancee. Kidnapped and brainwashed by Poseidal via bio-relation; reappear... | Under mind control she is cold and obedient, acting on Poseidal's orders; underneath sh... | 12 |
| ダバ・マイロード | Daba Myroad | ダバ = Daba | male | Protagonist. Heir of the Yaman clan's Kamon dynasty (true name Kamon Myroad), raised on Koam; leads the reb... | Calm, earnest and somewhat reserved, hard to read; indecisive at times but prone to sud... | 8 |
| オルドナ・ポセイダル | Oldna Poseidal | ポセイダル = Poseidal | female | Emperor ruling the Pentagona World from Sveto on Gastogal; supreme commander of the Poseidal Army. The Pose... | Regal, cold and imperious ruler who controls others (e.g. Quwasan) through the bio-rela... | 3 |
| ギワザ・ロワウ | Giwaza Lowau | ギワザ = Giwaza | male | Seat no. 3 and de facto leader of Poseidal's Thirteen, the highest-ranking officer after Poseidal; rebels a... | Capable, cold, calculating and ambitious; uses and discards people, including his lover... | 2 |
| ガウ・ハ・レッシィ | Gaw Ha Leccee | レッシィ = Leccee | female | Daughter of the noble Gaw house and a rising member of Poseidal's Thirteen; defects to Daba's rebels. Later... | Bold, headstrong and reckless yet emotionally fragile; competes with Amu for Daba; beco... | 1 |
| ギャブレット・ギャブレー | Gavlet Gablae | ギャブレー = Gablae | male | Daba's rival. Ambitious country noble from Koam who joins the Poseidal military (under Chai Char, later one... | Pompous and vain but sincere, warm-hearted and quick to fall in love; naive and comical... | 1 |
| ファンネリア・アム | Fanneria Amu | アム = Amu | female | Would-be stage actress turned bandit who leaves the Miyama Lilin gang to join Daba. Later captains the shut... | Devoted to Daba and determined to be useful; not very talented at first but works hard;... | 1 |
| ミラウー・キャオ | Mirao Kyao | キャオ = Kyao | male | Daba's childhood friend and travelling companion; the group's mechanic (rebuilt the stolen AD Stack into th... | Goofy, girl-crazy, carefree joker; a big eater who is surprisingly strong; loyal friend... | 1 |

### Blue Comet SPT Layzner

| Japonês | Inglês | Forma curta | Gênero | Papel | Personalidade (voz) | Ocorr. |
|---|---|---|---|---|---|---|
| ル・カイン | Le Cain |  | male | Son of Admiral Gresco; supreme commander of the Grados Earth occupation forces in the second arc; Eiji's ri... | Arrogant and ruthless, convinced of Gradosian racial and cultural superiority, yet prou... | 20 |
| レイ | Rei |  |  | The Layzner's onboard AI computer (speaks in short system reports) |  | 14 |
| ゴステロ | Gosterro |  | male | Grados lieutenant sent after Eiji (pilots the Bullgrenn). Rebuilt as a cyborg after his apparent death, he... | Sly, cruel sadist who enjoys killing; kills his own subordinates and frames others; ven... | 13 |
| エイジ・アスカ | Eiji Asuka | エイジ = Eiji | male | Protagonist. Half-Gradosian, half-human son of astronaut Ken Asuka; deserts Grados with the SPT Layzner to... | A gentle pacifist who hates killing, torn between protecting Earth and fighting his own... | 4 |
| アルバトロ・ナル・エイジ | Albatro Null Eiji | エイジ = Eiji | male | Protagonist Eiji Asuka's Grados name without the surname; half-Grados son of Ken Asuka who pilots the Layzner. |  | 3 |
| アルバトロ・ナル・エイジ・アスカ | Albatro Null Eiji Asuka | エイジ = Eiji | male | Full Gradosian name of Eiji Asuka (Albatro Null is his Grados name, Eiji his human name). | See Eiji Asuka. | 2 |
| ケン・アスカ | Ken Asuka |  | male | Eiji's father: a human astronaut, lost in deep space and found by the Grados, who opposes the invasion and... |  | 1 |

### Brain Powerd

| Japonês | Inglês | Forma curta | Gênero | Papel | Personalidade (voz) | Ocorr. |
|---|---|---|---|---|---|---|
| 伊佐未勇 | Yuu Isami | 勇 = Yuu | male | Male lead; former Reclaimer who escapes Orphan and pilots Yuu Brain, later Nelly Brain, for Novis Noah | Brooding lone wolf who resents his scientist parents. Often acts alone, but values life... | 6 |
| ユウ | Yuu |  | male | Short name of Yuu Isami (伊佐未勇), the male lead; pilots Yuu Brain. | Brooding lone wolf who resents his scientist parents; comes to value life and fights to... | 5 |
| ジョナサン・グレーン | Jonathan Glenn | ジョナサン = Jonathan | male | Reclaimer ace of Orphan; pilots Jonathan Grand Cher, later Jonathan Baronz; Yuu's rival and the son of Novi... | Arrogant, aggressive and taunting, full of resentment toward Yuu and his own mother. Lo... | 4 |
| 宇都宮比瑪 | Hime Utsumiya | 比瑪 = Hime | female | Female lead; 17-year-old Brain Powerd pilot (Hime Brain) aboard the Novis Noah | Cheerful, warm and motherly toward the children and her Brain. Optimistic and brave, an... | 4 |
| アイリーン・キャリアー | Irene Carrier | アイリーン = Irene | female | Ship's doctor (also an acupuncturist and former top military officer) on Novis Noah; becomes its captain af... | Calm, capable and motherly; a steady leader the pilots, especially Hime, look up to. | 3 |
| クインシィ・イッサー | Quincy Issa | クインシィ = Quincy | female | Reclaimer leader at Orphan; Yuu's older sister (real name Iiko Isami); pilots Quincy Grand Cher, later Quin... | Harsh, domineering and emotionally unstable. She denies her past as Iiko and resents Yu... | 3 |
| バロン・マクシミリアン | Baron Maximilian | バロン = Baron | female | Masked figure who seizes control of Orphan in Jonathan's name and gives him the Baronz; secretly Anoa McCor... | Mysterious, theatrical and manipulative. Acts as a mentor to Jonathan, driven by a twis... | 3 |

### Martian Successor Nadesico (TV / Prince of Darkness)

| Japonês | Inglês | Forma curta | Gênero | Papel | Personalidade (voz) | Ocorr. |
|---|---|---|---|---|---|---|
| テンカワ | Tenkawa |  | male | Surname of Akito Tenkawa; used alone (テンカワ君, テンカワ機 = Tenkawa's unit). |  | 15 |
| ヤマダ | Yamada |  | male | Surname of Jiro Yamada (who calls himself Gai Daigoji); used alone (ヤマダさん). |  | 8 |
| ミスマル・ユリカ | Yurika Misumaru | ユリカ = Yurika | female | Captain of the ND-001 Nadesico; Akito's childhood friend and later wife; prisoner of the Martian Successors... | Cheerful, airheaded and clingy toward Akito, but a genuinely brilliant tactician | 5 |
| ホシノ・ルリ | Ruri Hoshino | ルリ = Ruri | female | TV: operator/science officer of the Nadesico. PoD: Lieutenant Commander, captain of the Nadesico B ("Electr... | Deadpan, cool, blunt child prodigy (catchphrase "bunch of fools"); slowly warms to the... | 3 |
| 北辰 | Hokushin |  | male | Leader of the Martian Successors' assassin squad (Hokushin and his six men); Yatenkou pilot; kidnapped Akit... | Sadistic, cold, ruthless assassin; a master of both hand-to-hand and mecha combat | 3 |
| 白鳥九十九 | Tsukumo Shiratori | 白鳥 = Shiratori | male | Lieutenant Commander in the Jovian Superior Jovian Male Forces; Tetsujin/Daitetsujin pilot; seeks peace wit... | Honest, upright and idealistic, naive around women; hot-blooded Gekiganger fan | 3 |
| イネス・フレサンジュ | Inez Fressange | イネス = Inez | female | Nergal scientist aboard the Nadesico (Mars survivor); explains the technology | Brilliant, self-absorbed lecturer who loves giving "explanations"; secretly the grown-u... | 2 |
| ダイゴウジ・ガイ | Gai Daigoji | ガイ = Gai | male | Original Aestivalis pilot of the Nadesico (real name Jiro Yamada); killed early in the TV series | Loud, hot-blooded, obsessed with Gekiganger III; insists Gai is his soul's name | 2 |
| テンカワ・アキト | Akito Tenkawa | アキト = Akito | male | TV: cook and Aestivalis pilot of the Nadesico, a Class-A Boson Jumper. PoD: the "Prince of Darkness", Black... | TV: kind, reluctant and insecure Gekiganger fan who wants to be a cook. PoD: cold, grim... | 2 |
| ミスマル・コウイチロウ | Kouichiro Misumaru | ミスマル = Misumaru | male | Admiral of the United Earth forces (Third Fleet); Yurika's father; senior UESF commander in PoD | Doting, emotional father; stern but decent commander | 2 |
| ヤマダ・ジロウ | Jiro Yamada |  | male | Real name of Gai Daigoji (ダイゴウジ・ガイ), the hot-blooded Aestivalis pilot. | Loud, hot-blooded Gekigangar otaku who insists 'Gai' is his soul's name and hates being... | 2 |
| アカツキ・ナガレ | Nagare Akatsuki | アカツキ = Akatsuki | male | Aestivalis pilot who is secretly the chairman of Nergal Heavy Industries | Flippant playboy; cynical, calculating businessman | 1 |
| アマノ・ヒカル | Hikaru Amano | ヒカル = Hikaru | female | Aestivalis pilot of the Nadesico (orange frame); a manga artist by PoD | Bubbly, energetic otaku and Gekiganger fan; teases Ryoko | 1 |
| スバル・リョーコ | Ryoko Subaru | リョーコ = Ryoko | female | Leader of the Nadesico's Aestivalis squad (red 0G frame) | Hot-headed, tough, brash tomboy; respects only people who prove themselves; secretly sw... | 1 |
| マキ・イズミ | Izumi Maki | イズミ = Izumi | female | Aestivalis pilot of the Nadesico (green frame); a bar musician by PoD | Gloomy, eerie, incurable punster; has a hidden serious side | 1 |
| 月臣元一郎 | Genichirou Tsukiomi | 月臣 = Tsukiomi | male | Officer of the Jovian Superior Jovian Male Forces (Yuujin Butai), Majin/Daimajin pilot; in PoD a Nergal ope... | Proud, serious, intensely idealistic; haunted by having shot his friend Tsukumo | 1 |

### Metal Armor Dragonar

| Japonês | Inglês | Forma curta | Gênero | Papel | Personalidade (voz) | Ocorr. |
|---|---|---|---|---|---|---|
| ギガノス | Giganos |  | not applicable | Faction: Unified Lunar Empire of Giganos (旧ギガノス士官 = former Giganos officer) |  | 116 |
| ドルチェノフ | Dorchenov |  | male | Giganos hardliner; as Lieutenant Colonel he assassinates Marshal Guiltorre and becomes Supreme Leader of Gi... | Arrogant, power-hungry, cruel and treacherous; bullies subordinates; strong MA pilot bu... | 20 |
| グン・ジェム | Gon Jem |  | male | Giganos Colonel commanding the Gon Jem Squad (the "Filth of Giganos"); pilots the Geyzam, later the prototy... | Brutal, crude, greedy and cunning, with famously bad table manners; superb pilot; fierc... | 14 |
| ミン | Min |  | female | Giganos Captain, the only woman among Gon Jem's Four Kings; Stark Dyne pilot; later joins Meio | Fierce, violent and battle-hungry; later shows a devoted, gentler side toward Meio | 10 |
| ギルトール | Guiltorre |  | male | Marshal Iskander Guiltorre, leader of the Giganos Empire, assassinated in the story. |  | 9 |
| マイヨ・プラート | Meio Plato | マイヨ = Meio | male | Captain and top ace of the Giganos Imperial Guard armored corps ("Blue Hawk of Giganos"); Falguen pilot; fr... | Noble, calm and honorable; devoted to Marshal Guiltorre; resents his father Lang for de... | 8 |
| ケーン・ワカバ | Kaine Wakaba | ケーン = Kaine | male | Pilot of Dragonar-1 (D-1); Earth Alliance/Federation trainee promoted to Warrant Officer; protagonist | Hot-blooded, impulsive, acts before thinking; chases Linda; resents his absent father | 6 |
| ギルトール元帥 | Marshal Guiltorre |  | male | Marshal and supreme leader of Giganos; assassinated by Dorchenov | Idealistic and honorable; loves Earth's beauty and restrains use of the Mass Driver | 5 |
| リンダ・プラート | Linda Plato | リンダ = Linda | female | Meio's younger sister; refugee who becomes an Earth Alliance communications operator; heroine | Gentle and reserved, opposes the war; slowly opens up to Kaine | 2 |
| アオイ・ワカバ | Aoi Wakaba |  | female | Kaine's mother, administrator of the colony Alucard; captured by Giganos and used as leverage against Kaine. |  | 1 |
| タップ・オセアノ | Tapp Oceano | タップ = Tapp | male | Pilot of Dragonar-2 (D-2, long-range artillery); Kaine's best friend | Cheerful, laid-back New Yorker; loyal and family-minded (sends his pay home); serious w... | 1 |
| ライト・ニューマン | Light Newman | ライト = Light | male | Pilot of Dragonar-3 (D-3, electronic warfare/recon); Kaine's friend | Cheerful, quick-witted, the level head of the trio; rebels against his British politica... | 1 |

### Another Century's Episode (original)

| Japonês | Inglês | Forma curta | Gênero | Papel | Personalidade (voz) | Ocorr. |
|---|---|---|---|---|---|---|
| アルバート・ライネン | Albert Rainen | ライネン = Rainen | male | Former UCE scientist who warned of alien invasion and led the satellite-cannon defense project (Rainen Proj... | Visionary 'ignored expert' embittered by the UCE's dismissal of his warnings. | 12 |
| マリナ・カーソン | Marina Carson | マリナ = Marina | female | ACE2 heroine; Ensign in Tak's squad, pilot of the red Gun Ark; goes missing at Torrington Base, reappears w... | Cool and reserved ('defrosting ice queen' in flashbacks); deeply bonded with Tak. | 6 |
| タック・ケプフォード | Tak Kepford | タック = Tak | male | ACE2 protagonist; UCE squad leader (First Lieutenant) and Gun Ark test pilot, joins the Albion unit. | Skilled ace and natural leader, but clumsy with machines (mechanically inept); grows su... | 5 |
| バルクホルツ博士 | Dr. Barkholz | バルクホルツ = Barkholz | male | Same person as Fidel Barkholz (title form). |  | 5 |
| タック&マリナ | Tak & Marina |  |  | Combined speaker label for Tak and Marina speaking together. |  | 2 |
| フィーデル・バルクホルツ | Fidel Barkholz | バルクホルツ = Barkholz | male | UCE Design Bureau engineer in charge of Ark-series/Gun Ark development; supports Tak and Marina. Spoiler: s... | Outwardly a kindly professor-type adviser (sends Tak e-mails); actually vengeful agains... | 1 |

## Unidades (mechas)

### Mobile Suit Gundam 0083: Stardust Memory

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| GP02 | GP02 | Gundam Development Project Unit 2, RX-78GP02A Gundam "Physalis", the nuclear-armed Gundam stolen by Gato. | 16 |
| ガンダム試作2号機 | Gundam GP02 | RX-78GP02A Gundam "Physalis". | 10 |
| ノイエ・ジール | Neue Ziel | AMX-002 (AMA-X2), giant Zeon mobile armor flown by Gato in the finale. | 10 |
| ゲルググM | Gelgoog Marine | MS-14F, marine-corps Gelgoog flown by the Cima Fleet. | 9 |
| ガンダム試作3号機 | Gundam GP03 | RX-78GP03 Gundam "Dendrobium" (Stamen MS plus Orchis armed base), flown by Kou in space. | 7 |
| ガンダム試作1号機 | Gundam GP01 | RX-78GP01 Gundam "Zephyranthes", Kou's Gundam. | 5 |
| ガーベラ・テトラ | Gerbera Tetra | AGX-04, Anaheim prototype (the GP04 Gerbera rebuilt) handed to Cima. | 3 |
| ゲルググM(シーマ) | Gelgoog Marine (Cima) | Cima Garahau's personal unit, the MS-14Fs Gelgoog Marine Commander Type. | 3 |
| ドラッツェ | Dra-C | MS-21C, Delaz Fleet assault suit built from Zaku II F2 bodies and Gattle fighter parts. | 3 |
| ザクIIF2型 | Zaku II F2 Type | MS-06F-2, late-war Zaku II variant used widely by Zeon remnants and the Delaz/Cima fleets. | 2 |
| ザクIIF2型(ろ獲機) | Zaku II F2 Type (Captured) | Zaku II F2 Type captured and flown by the Earth Federation (used as training/aggressor units after the war). | 1 |

### Mobile Suit Gundam: Char's Counterattack

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| νガンダム | Nu Gundam |  | 6 |
| サザビー | Sazabi | MSN-04, Char's Neo Zeon Newtype mobile suit. | 5 |
| リ・ガズィ | Re-GZ |  | 5 |
| リ・ガズィ(BWS) | Re-GZ (BWS) |  | 2 |
| リガズィ | Re-GZ |  | 1 |

### Mobile Suit Zeta Gundam

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ハイザック | Hizack | RMS-106, Federation/Titans mass-production suit derived from the Zaku design. | 1 |
| マラサイ | Marasai | RMS-108 (MSA-002), Anaheim-built suit flown by the Titans. | 1 |

### Mobile Fighter G Gundam

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| デビルガンダム | Devil Gundam | Self-evolving, self-repairing, self-replicating rogue Gundam (JDG-00X); main antagonist machine of G Gundam | 42 |
| ゴッドガンダム | God Gundam | Domon's second Mobile Fighter (GF13-017NJII), Neo Japan; God Finger and Hyper Mode (Meikyo Shisui) | 13 |

### Mobile Suit Gundam Wing / Endless Waltz

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| トールギス | Tallgeese | Prototype high-performance mobile suit (OZ-00MS), Zechs's machine | 8 |
| ウイングガンダムゼロ | Wing Gundam Zero | Heero's Gundam (XXXG-00W0) with the ZERO System and Twin Buster Rifle | 5 |
| ガンダムナタク | Gundam Nataku | Chang Wufei's Gundam (XXXG-01S2), Endless Waltz redesign of Altron Gundam; fought as an enemy in ACE2 missi... | 5 |
| サーペント | Serpent | Mass-produced heavy-firepower mobile suit (MMS-01) of the Mariemaia Army | 5 |
| トールギスIII | Tallgeese III | Final Tallgeese variant (OZ-00MS2B) with a Mega Cannon, piloted by Zechs in Endless Waltz | 5 |
| エアリーズ | Aries | Mass-produced aerial mobile suit (OZ-07AMS) | 4 |
| ガンダムサンドロック | Gundam Sandrock | Quatre's desert-combat Gundam (XXXG-01SR) with Heat Shotels | 3 |
| ガンダムデスサイズヘル | Gundam Deathscythe Hell | Duo's upgraded Gundam (XXXG-01D2) with Active Cloak and Twin Beam Scythe | 3 |
| ガンダムヘビーアームズ | Gundam Heavyarms | Trowa's heavy-firepower Gundam (XXXG-01H) | 3 |
| ビルゴ | Virgo | Mass-produced AI-controlled mobile doll (OZ-02MD) with planet defensors | 2 |
| リーオー | Leo | Mass-produced general-purpose mobile suit (OZ-06MS), also used by the Mariemaia Army | 2 |
| ウイングガンダムゼロ(EW版) | Wing Gundam Zero (EW) | Endless Waltz version of Wing Gundam Zero (Wing Zero Custom) | 1 |
| ガンダムサンドロック(EW版) | Gundam Sandrock (EW) | Endless Waltz version of Sandrock | 1 |
| ガンダムデスサイズヘル(EW版) | Gundam Deathscythe Hell (EW) | Endless Waltz version of Deathscythe Hell | 1 |
| ガンダムヘビーアームズ(EW版) | Gundam Heavyarms (EW) | Endless Waltz version of Heavyarms | 1 |

### Gundam (Universal Century, geral)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ザクII | Zaku II | Zeon's main mass-production mobile suit (MS-06). | 4 |

### Super Dimension Fortress Macross: Do You Remember Love?

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| バルキリー | Valkyrie | U.N. Spacy VF-1 variable fighter series. | 18 |
| クァドラン・ロー | Queadluun-Rau | Meltrandi high-maneuver battle suit; Milia's machine. | 9 |
| VF-1J | VF-1J |  | 7 |
| クァドラン・ロー(ミリア) | Queadluun-Rau (Milia) |  | 4 |
| ヌージャデル・ガー | Nousjadeul-Ger | Zentradi general-issue powered suit (DYRL design). | 4 |
| アーマードバルキリー | Armored Valkyrie |  | 3 |
| グラージ | Glaug | Zentradi officer/commander battle pod. | 3 |
| リガード | Regult | Standard Zentradi mass-production battle pod. | 2 |

### Aura Battler Dunbine / The Wings of Rean

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ダンバイン | Dunbine | Title Aura Battler; Sho's first unit; Marvel's playable unit in ACE2 | 12 |
| レプラカーン | Leprechaun | Heavily armed Drake army Aura Battler; Jeryll's unit in ACE2 | 8 |
| ビルバイン | Billbine | Sho's upgraded, transformable Aura Battler from the Kingdom of Na; Sho's playable unit in ACE2 (also a camo... | 7 |
| ズワァース | Zwarth | Most powerful late-war Drake Aura Battler; the Black Knight's unit | 6 |
| ライネック | Wryneck | Late-war Aura Battler of the Drake and Kingdom of Kuh side (Bishot Hate); Todd's unit in ACE2 | 5 |
| ガラバ | Galava | Aura Fighter (not humanoid); the Black Knight's second unit in ACE2 | 4 |
| バストール | Bastole | Drake army Aura Battler (Garalia's pink custom in the series) | 4 |
| オウカオー | Oukaou |  | 3 |
| ハイパーライネック | Hyper Wryneck | Giant 'Hyper' form of the Wryneck (boss unit; Todd's hyper-ized Wryneck) | 3 |
| ドラムロ | Drumlo | Drake army mass-production Aura Battler (grunt unit) | 2 |
| ビアレス | Vierres | Drake army high-performance Aura Battler | 2 |
| ビランビー | Virunvee | Drake army Aura Battler (Garalia's and Burn's unit in the series) | 2 |
| ビルバイン迷彩カラー | Billbine (Camouflage) |  | 2 |

### Heavy Metal L-Gaim

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| エルガイム | L-Gaim | Daba's white A-class Heavy Metal, a Yaman-built mecha. Later piloted by Amu. | 16 |
| アトール | A-Taul | High-output Poseidal Army A-class Heavy Metal capable of solo flight; one of Gavlet Gablae's units (playabl... | 8 |
| アシュラ・テンプル | Ashura Temple | Poseidal Army Temple-series A-class Heavy Metal with four Power Launchers; piloted by Gavlet Gablae (his AC... | 7 |
| オージ | Aug | The true Poseidal's personal Heavy Metal (the 'Original Auge'), built from Auge/Blood Temple/Pudding Auge p... | 5 |
| バッシュ | Bat-Shu | Poseidal Army A-class Heavy Metal (one of a dozen replicas of a lost original); piloted by Gavlet Gablae an... | 5 |
| カルバリー・テンプル | Calvary Temple | Poseidal Army Temple-series A-class Heavy Metal with a chest laser reflector; Quwasan Olibee's unit (copper... | 4 |
| グライア | Graia | Graia, Poseidal Army mass-production Heavy Metal | 4 |
| エルガイムMk-II | L-Gaim Mk-II | Daba's second Heavy Metal, a transformable unit rebuilt from the Amon Duule Stack and armed with the Buster... | 3 |
| ファルゲン・マッフ | Falguen MAFFU |  | 3 |
| アトールV | A-Taul V | Custom A-Taul ('A-Taul Five', McTomin Build) of Thirteen member Maph McTomin, fitted with replica armaments... | 2 |
| オージェ | Auge | Poseidal Army A-class Heavy Metal (replica of a Poseidal-family unit); main pilot Nei Mo Han. | 2 |
| グルーン | G.Roon | Mass-produced Poseidal Army A-class Heavy Metal armed with a remote-operated long spear; pilots include Nei... | 2 |
| スペース・グライア | Space Graia | Space-use variant of the Graia | 2 |

### Blue Comet SPT Layzner

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| レイズナー | Layzner | SPT-LZ-00X, Eiji's experimental Grados SPT with the AI 'Rei' and the V-MAX system. | 22 |
| レイズナーMk-II | Layzner Mk-II | E-MF-LZ-00X-2, the Earth-built successor design for Eiji that went unused in the TV series (the show was cu... | 9 |
| エルダール | El Darr | Shikitai (死鬼隊) custom MF of the Grados army, enemy in m6221 ('行け、エルダール!'). | 8 |
| ガッシュラン | Gashlan | Shikitai custom MF of the Grados army (m6221 '行け、ガッシュラン!'). | 8 |
| ダンコフ | Dankova | Shikitai custom MF of the Grados army (m6221 '行け、ダンコフ!'). | 8 |
| ターミネーターポリス | Terminator Police | TS-TP-50D, unmanned Grados Terror Striker developed from the Skull Gunner and used to hunt Earth's resistan... | 7 |
| ダルジャン | Daljuan | MF-DJ-91U, Gosterro's custom Multi-Form unit as a Shikitai (Death Demon Squad) member, armed with a laser b... | 5 |
| ザカール | Zakaal | SPT-ZK-53U, Le Cain's gold custom SPT, the strongest Grados SPT, with a sealed V-MAX. | 4 |
| ブルグレン | Bullgrenn | SPT-BG-91U, Grados commander-type SPT; Gosterro's unit in the first arc (playable for him in ACE2). | 4 |
| ディマージュ | Dimarge | SPT-DM-20C, high-mobility mass-production Grados SPT (Karla Egiel's unit; widely used during the Earth occu... | 3 |
| ブレイバー | Braver | SPT-BV-15C Braver, a Grados SPT (grunt). It appears among the Layzner units in the ACE2 unit list (between... | 3 |
| グライムカイザル | Grimekaisar | SPT-GK-10U, Grados senior-officer SPT; Ahmos Gale's personal unit, specialized for space combat. Enemy unit. | 2 |
| スカルガンナー | Skull Gunner | TS-SG-50C, Grados unmanned Terror Striker drone. Enemy unit. | 2 |
| ソロムコ | Solomco | MF-SL-52C, Grados mass-production Multi-Form unit for atmospheric use that transforms between aircraft and... | 2 |

### Brain Powerd

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| グランチャー | Grand Cher | Orphan-loyal Antibody piloted by Reclaimers (generic grunt unit) | 27 |
| バロンズゥ | Baronz | Dotless form of バロン・ズゥ: Jonathan's/Quincy's powerful Antibody (also 巨大バロンズゥ). | 17 |
| ブレンパワード | Brain Powerd | The type of Antibody that rebels against Orphan; generic Brain Powerd unit (also the series title) | 11 |
| ヒメ・ブレン | Hime Brain | Hime Utsumiya's Brain Powerd | 8 |
| クインシィ・バロンズゥ | Quincy Baronz | Baronz that evolved from Quincy's Grand Cher; Quincy's playable unit in ACE2 | 6 |
| クインシィ・グランチャー | Quincy Grand Cher | Quincy Issa's red custom Grand Cher | 5 |
| ジョナサン・バロンズゥ | Jonathan Baronz | Evolved Antibody that Baron Maximilian gives to Jonathan Glenn | 5 |
| ユウ・ブレン | Yuu Brain | Yuu Isami's Brain Powerd | 5 |
| ジョナサン・グランチャー | Jonathan Grand Cher | Jonathan Glenn's custom Grand Cher | 4 |
| バロン・ズゥ | Baronz | Evolved Antibody created by reviving a Grand Cher (e.g. Jonathan Baronz, Quincy Baronz). | 4 |
| アーミー・グランチャー | Army Grand Cher | Grand Cher flown by US military forces occupying Orphan | 3 |
| ネリー・ブレン | Nelly Brain |  | 3 |
| ジョナサングランチャー | Jonathan Grand Cher | Same unit as ジョナサン・グランチャー; this game string just has no middle dot | 2 |

### Martian Successor Nadesico (TV / Prince of Darkness)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| エステバリス | Aestivalis | Nergal mass-produced mecha; used alone and in エステバリス隊 (Aestivalis squad/team). | 51 |
| ナナフシ | Nanafushi | Jovian 'new weapon' (micro black hole railgun) that the player must destroy (mission 新型兵器ナナフシ). | 24 |
| ダイマジン | Daimajin | Upgraded Jovian Majin (Tsukiomi) | 10 |
| ダイテツジン | Daitetsujin | Upgraded Jovian Tetsujin (Tsukumo; later Takasugi) | 8 |
| ブラックサレナ | Black Sarena | Akito's armored, high-mobility custom Aestivalis in Prince of Darkness | 5 |
| エステバリス(アキト) | Aestivalis (Akito) | Akito's Aestivalis (TV series) | 4 |
| アルストロメリア | Alstroemeria |  | 3 |
| デビルエステバリス | Devil Aestivalis | Hijacked mass-production Aestivalis controlled by Jovian Batta (enemy unit) | 3 |
| ナナジン | Nanajin |  | 3 |
| マジン | Majin | Jovian manned mecha (Genichirou Tsukiomi) | 3 |
| 夜天光 | Yatenko | Hokushin's personal mecha in Prince of Darkness (leads the Rokuren units) | 3 |
| アキトバリス | Akitovalis | Akito's custom Aestivalis left when the Black Sarena purges its armor (listed right after Black Sarena in t... | 2 |
| エステバリス(ガイ) | Aestivalis (Gai) | Gai's Aestivalis (TV series) | 2 |
| エステバリスC(イズミ) | Aestivalis C (Izumi) |  | 2 |
| エステバリスC(ヒカル) | Aestivalis C (Hikaru) |  | 2 |
| エステバリスC(リョーコ) | Aestivalis C (Ryoko) |  | 2 |
| テツジン | Tetsujin | Jovian manned mecha (Tsukumo Shiratori) | 2 |
| 高機動型ブラックサレナ | Hi-Mob. Black Sarena |  | 2 |
| エステバリス(アキト専用機) | Aestivalis (Akito C.) |  | 1 |

### Metal Armor Dragonar

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ファルゲン | Falguen | XFMA-09 Falguen, Meio Plato's personal blue-purple Metal Armor | 14 |
| ギルガザムネ | Gilgazamune | YGMA-14 Gilgazamune, giant thought-controlled Metal Armor (Gon Jem's prototype; Heidelnecken and Dorchenov... | 9 |
| ダイン | Deins | FMA-04A Dyne, standard Giganos mass-production Metal Armor | 9 |
| D-1 | D-1 | XD-01 Dragonar-1 (Kaine), close-combat type | 8 |
| ゲバイ | Gwei | AMA-03B Gwei, widely used heavy Giganos mass-production Metal Armor | 8 |
| スターク・ダイン | Stark Deins | FMA-04G Stark Dyne, Min's custom Dyne with arm chainsaws | 5 |
| ダウツェン | Dowtwen | AFA-03 Dowtwen, Giganos atmospheric unit halfway between Metal Armor and Folg | 5 |
| ゲイザム | Geyzam | YAMA-13 Geyzam, Gon Jem's one-off prototype Metal Armor | 4 |
| ゲルフ | Gelf | YFMA-08A Gelf, Dan Kruger's Metal Armor (Practice Squad) | 3 |
| スターク・ガンドーラ | Stark Gan Dolla | Stark Gan Dolla, Ganan's custom Gan Dolla (splits into robot and motorcycle) | 3 |
| ドラグナー1型カスタム | Dragonar-1 Custom |  | 3 |
| ドラグナー2型カスタム | Dragonar-2 Custom |  | 3 |
| ドラグナー3型(後期型) | Dragonar-3 (Late Model) |  | 3 |
| ヤクトゲルフ | Jagd Gelf | YAMA-08B Jagd Gelf, Welner Fritz's artillery variant of the Gelf | 3 |
| レビゲルフ | Reb Gelf | YRMA-08C Reb Gelf, Karl Geiner's ECM variant of the Gelf | 3 |
| D-1カスタム | D-1 Custom | XD-01SR Dragonar-1 Custom (Kaine) | 2 |
| スターク・ゲバイ | Stark Gwei | AMA-03G Stark Gwei, Gol's custom Gwei | 2 |
| スターク・ダウツェン | Stark Dowtwen | AFA-03G Stark Dowtwen, Zin's custom Dowtwen with hologram decoys | 2 |
| ズワイ | Zuwai | WAMA-07A Zuwai, Giganos amphibious close-combat Metal Armor | 2 |
| ゲバイSP | Gwei SP | ACE2 variant of the Gwei (the game also lists ゲバイ（ＳＰ） and ゲバイ・マッフ（ＳＰ）) | 1 |

### Another Century's Episode (original)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| バスターアーク | Buster Ark | Modified Gun Ark with an evolving Guardian System and fallen-angel styling; Marina's unit while with the Ra... | 71 |
| ガンアーク | Gun Ark | Latest Ark-series transforming machine from the UCE Design Bureau; Tak's (and initially Marina's red) unit;... | 36 |
| ザロム | Zarom | ACE2 original enemy (FromSoftware design), one of the 'Rainen series' of autonomous units developed by the... | 6 |
| ザロムD | Zarom D | ACE2 original enemy (FromSoftware design): upgraded Zarom (Rainen series) with an added defensive field. | 4 |
| フェザーアーク | Feather Ark | First Ark-series machine; discontinued high-performance Guardian System unit; secret unit playable by Marina. | 3 |
| フェザーアークカスタム | Feather Ark Custom | Barkholz's customized, greatly strengthened Feather Ark (final boss machine). | 3 |
| グノスト | Gnost | ACE original enemy (Banpresto design): upgraded infantry unit derived from the Risnir, with a left-arm gatl... | 2 |
| シアスィ | Thiassi | ACE original enemy (Banpresto design): air-combat fire-support unit resembling an Apache helicopter crossed... | 2 |
| レーヴェ | Loewe | ACE original enemy (FromSoftware design): heavy-artillery unit whose entire right arm is a large cannon; lo... | 2 |
| ヴァーゲ | Waage | ACE original enemy (FromSoftware design): flight-capable unit specializing in mobile bombardment. A UCE pro... | 2 |
| UNKNOWN | UNKNOWN |  | 1 |

## Naves

### Mobile Suit Gundam 0083: Stardust Memory

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| アルビオン | Albion | MSC-07 Pegasus-class Federation assault carrier commanded by Sinapus. | 156 |
| ラビアンローズ | La Vie en Rose | Anaheim Electronics mobile docking ship where Kou receives GP03. | 8 |
| コムサイII | Komusai II |  | 5 |

### Mobile Suit Gundam: Char's Counterattack

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ラーカイラム | Ra Cailum | Bright Noa's flagship, dotless spelling used in m6900. | 6 |
| ラー・カイラム | Ra Cailum | Londo Bell flagship battleship (Bright Noa's ship) in CCA. | 6 |
| ムサカ | Musaka | Neo Zeon light cruiser class in CCA. | 2 |
| レウルーラ | Rewloola | Neo Zeon flagship battleship (Char's ship) in CCA. | 2 |

### Gundam (Universal Century, geral)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ホワイトベース | White Base |  | 2 |

### Super Dimension Fortress Macross: Do You Remember Love?

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| マクロス | Macross | SDF-1 Macross, the U.N. Spacy super-dimensional fortress (human flagship). | 108 |
| ブリタイ艦 | Vrlitwhai's Ship | Vrlitwhai's fleet command battleship. | 6 |
| ボドル旗艦 | Boddole Flagship | Boddole Zer's gigantic mobile-fortress flagship (DYRL final boss). | 3 |

### Aura Battler Dunbine / The Wings of Rean

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| グラン・ガラン | Gran-Garan | Aura battleship of Queen Ciela Lapana (Kingdom of Na) | 30 |
| ゴラオン | Goraon | Aura battleship of Elle Humm (Kingdom of Lao), armed with the Aura Nova Cannon | 19 |
| ウィル・ウィプス | Will Wipps | Drake Luft's flagship aura battleship; an enemy ship in Operation 25. | 13 |
| ゲア・ガリング | Gea Garing | Aura battleship of Bishot Hatta, King of Ku; an enemy ship in Operation 25. | 12 |
| ブル・ベガー | Bull Beggar | Class of Drake-side aura ship; a weaker cousin of the aura battleships. | 5 |

### Heavy Metal L-Gaim

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| サージェ・オーパス | Sarge Opus | Poseidal-side planetary cruiser; Giwaza Lowau's flagship class. ACE2 Op 23 objective: 'Destroy Sarge Opus'. | 2 |

### Brain Powerd

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ノヴィス・ノア | Novis Noah | Anti-Orphan battleship (carrier with a pyramid superstructure); base of the Brain Powerd pilots | 55 |

### Martian Successor Nadesico (TV / Prince of Darkness)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ナデシコ | Nadesico | ND-001 Nadesico, Nergal's battleship | 222 |
| ナデシコB | Nadesico B | NS-955B Nadesico B, second-generation Nadesico-class battleship of the UESF captained by Ruri | 14 |

## Facções e organizações

### Mobile Suit Gundam 0083: Stardust Memory

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| デラーズ・フリート | Delaz Fleet | Zeon remnant force led by Aiguille Delaz that carries out Operation Stardust in U.C. 0083. | 29 |

### Mobile Suit Gundam: Char's Counterattack

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ロンド・ベル | Londo Bell | Earth Federation Forces special task force of the UC 0090s (Amuro, Bright, Ra Cailum). | 1 |

### Mobile Suit Gundam Wing / Endless Waltz

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| プリベンター | Preventer | Secret intelligence/peacekeeping organization of the Earth Sphere Unified Nation that stops conflicts befor... | 22 |
| ホワイトファング | White Fang | Militant anti-Earth colony organization, later led by Zechs Merquise | 5 |
| OZ | OZ | Organization of the Zodiac: elite secret society/military organization inside the Alliance, led by Treize K... | 2 |

### Gundam (Universal Century, geral)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ジオン残党 | Zeon Remnants | Federation term for Zeon soldiers who kept fighting after the One Year War. | 15 |
| 旧ジオン公国 | former Principality of Zeon |  | 5 |
| アナハイム・エレクトロニクス | Anaheim Electronics | Lunar arms conglomerate that builds mobile suits for several factions; co-developer of the Gundam Developme... | 3 |

### Super Dimension Fortress Macross: Do You Remember Love?

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ゼントラーディ | Zentradi | Race/faction of giant humanoid warriors; main antagonists. | 59 |
| メルトランディ | Meltrandi | Female Zentradi faction, at war with the male Zentradi in DYRL. | 24 |
| ボドル | Boddole | Short for Boddole Zer's fleet: ボドル基幹艦隊 (main fleet), ボドル艦隊 (fleet), ボドル旗艦 (flagship). | 12 |
| ボドル艦隊 | Boddole Fleet | Same fleet, mission titles ボドル艦隊迎撃戦 I-III. | 6 |
| ボドル基幹艦隊 | Boddole Main Fleet | Boddole Zer's main Zentradi fleet that the Macross and Nadesico attack. | 2 |

### Heavy Metal L-Gaim

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ポセイダル軍 | Poseidal Army | The military of Emperor Poseidal that rules the Pentagona World; the main antagonist force of L-Gaim. | 14 |
| ギワザ艦隊 | Giwaza Fleet | Giwaza Lowau's rebel fleet (mostly Sarge Opus planet cruisers of the Thirteen) that turns against Poseidal. | 8 |

### Blue Comet SPT Layzner

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| グラドス | Grados | The alien Grados Empire, from the Udoria system, that invades and occupies Earth in Layzner. Adjective form... | 51 |
| グラドス地球制圧軍 | Grados Earth Subjugation Force | The Grados military forces conquering and occupying Earth (Admiral Gresco's, later Le Cain's, command). | 2 |

### Brain Powerd

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| リクレイマー | Reclaimer | The people who serve Orphan and pilot Grand Chers to gather its plates; plural 'Reclaimers' | 50 |

### Martian Successor Nadesico (TV / Prince of Darkness)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| 木星蜥蜴 | Jovian Lizards | Earth's name for the unknown Jovian enemy (actually the Jovian Federation, 木連). | 37 |
| 木連 | Jovian Federation | Jupiter-based anti-Earth state, main enemy faction of the TV series (romaji Mokuren) | 26 |
| ネルガル | Nergal | Short form of Nergal Heavy Industries (ネルガル側, ネルガルの戦艦ナデシコ). | 18 |
| ネルガル重工 | Nergal Heavy Industries | Corporation that built the Nadesico and the Aestivalis | 9 |
| 連合宇宙軍 | United Earth Space Force | Earth's unified space force after the war; operates the Nadesico B | 9 |

### Metal Armor Dragonar

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| 統一帝国ギガノス | Unified Empire of Giganos | Formal name of the lunar state that declared independence from Earth | 12 |
| ギガノス帝国 | Giganos Empire | Common short name of the Unified Empire of Giganos | 7 |
| グン・ジェム隊 | Gon Jem Squad | Gon Jem's irregular unit, nicknamed the "Filth of Giganos" | 3 |

### Another Century's Episode (original)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| UCE | UCE | United Community of Earth: the unified Earth government/military of the ACE setting (Japanese 地球統一機構, also... | 198 |

## Lugares

### Mobile Suit Gundam 0083: Stardust Memory

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| コンペイトウ | Konpei Island | The former Zeon fortress Solomon, renamed by the Federation; site of the 0083 naval review that Gato attacks. | 14 |
| トリントン基地 | Torrington Base | Federation base in eastern Australia where Gato steals GP02. | 8 |
| キンバライド | Kimbareid | Zeon remnant base in an African mine (キンバライド基地, キンバライド鉱山). | 7 |

### Aura Battler Dunbine / The Wings of Rean

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| バイストン・ウェル | Byston Well | The otherworld between sea and land where Dunbine takes place. | 20 |

### Heavy Metal L-Gaim

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ペンタゴナ | Pentagona | The Pentagona System / Pentagona World: the five-planet star system where L-Gaim is set (Koam, Mizum, Gasto... | 7 |
| ペンタゴナワールド | Pentagona World | Dotless form: the binary-star system Daba and Poseidal's army come from. | 7 |
| ペンタゴナ・ワールド | Pentagona World | The five-planet Pentagona system where L-Gaim is set. | 1 |

### Martian Successor Nadesico (TV / Prince of Darkness)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| サセボ | Sasebo | Japanese port city where the Nadesico is docked/launched (サセボドック, mission サセボ攻防戦). | 10 |

### Metal Armor Dragonar

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ギガノス要塞 | Giganos Fortress | Giganos fortress (ep. 21 title "ギガノス要塞破壊命令"; late in the series also the Giganos mobile space fortress) | 2 |

## Termos da série

### Mobile Suit Gundam 0083: Stardust Memory

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ガンダム開発計画 | Gundam Development Project | Top-secret EFF/Anaheim project that produced GP01-GP04. | 11 |
| クローアーム | claw arm | Neue Ziel's wired claw arms, fired from the main arms (有線クローアーム = Wired Claw Arm). | 10 |
| モビルアーマー | mobile armor | Large mobile weapon; in ACE2 it is Gato's Neue Ziel (大型モビルアーマー, missions モビルアーマー排除). | 10 |
| ソーラ・システム | Solar System | Earth Federation mirror-array superweapon that focuses sunlight. ACE2 Op 08 sub-mission 'Defending Solar Sy... | 8 |
| ソロモンの悪夢 | Nightmare of Solomon | Anavel Gato's epithet. ソロモン never appears alone in ACE2. | 6 |
| ソーラレイ | Solar Ray | Appears only in developer comment rows (※ソーラレイ防衛戦 喧騒感演出用) of the Solar System defense mission. | 6 |
| ミノフスキー粒子 | Minovsky particles | Radar-jamming particle scattered by Zeon forces (ミノフスキー粒子の散布!). | 3 |
| 星の屑作戦 | Operation Stardust | Delaz Fleet operation of U.C. 0083 (nuclear strike at Konpei Island followed by a colony drop). | 3 |
| ニュータイプ | Newtype | Psychically evolved human; said of Amuro (m6022#149) and Kou (m6033#103). | 2 |

### Mobile Suit Gundam: Char's Counterattack

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ファンネル | Funnel | Sazabi's remote psycommu weapon (Weapon 6); ν Gundam's version is フィン・ファンネル (Fin Funnel). | 9 |

### Mobile Fighter G Gundam

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| 明鏡止水 | Meikyo Shisui | God Gundam's higher state (明鏡止水モード) reached when Domon's heart attains a serene mind. | 12 |
| ハイパーモード | Hyper Mode | God Gundam's power-up state, triggered when Domon's fighting spirit gauge peaks (tutorial m6302#179-183). | 8 |
| モビルファイター | Mobile Fighter | G Gundam term for Gundam Fight mecha (Devil Gundam, Master Gundam...). | 5 |
| ガンダムファイト | Gundam Fight | The G Gundam tournament; announcer catchphrase ガンダムファイト!! レディーーー、ゴォーーー!! | 2 |
| キング・オブ・ハート | King of Hearts | Shuffle Alliance title held by Domon Kasshu (formerly Master Asia). | 2 |

### Mobile Suit Gundam Wing / Endless Waltz

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| リーンの翼 | Wings of Rean | Nanajin's ability (auto-activates at low armor; also usable as a barrier) and the series title (menu3022#12). | 14 |
| ハイパージャマー | Hyper Jammer | Gundam Deathscythe Hell's jamming device (Weapon 5): evades enemy lock-on for a time, drains vernier. | 6 |

### Gundam (Universal Century, geral)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| 大尉 | Captain | Military rank | 31 |
| 少尉 | Ensign | Military rank | 20 |
| 少佐 | Major | Military rank | 13 |
| 中尉 | Lieutenant Junior Grade | Military rank | 11 |
| 准将 | Commodore | Military rank | 10 |
| 元帥 | Fleet Admiral | Military rank | 7 |
| スペースノイド | Spacenoid |  | 4 |
| 中佐 | Lieutenant Colonel | Military rank | 4 |
| 一年戦争 | One Year War |  | 3 |
| 大佐 | Captain | Military rank | 3 |
| 中将 | Vice Admiral | Military rank | 1 |

### Super Dimension Fortress Macross: Do You Remember Love?

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| プロトカルチャー | Protoculture | Ancient precursor civilisation; the found song/poem plates are judged to be Protoculture artefacts. | 15 |
| ファイター | Fighter | Jet-fighter mode of the VF-1 Valkyrie (ファイター形態 = Fighter mode). | 12 |
| フォールド | fold | Space-jump (fold) drive of the Macross; Nadesico gets caught in the Macross space fold. | 11 |
| バトロイド | Battroid | Humanoid mode of the VF-1 Valkyrie (バトロイド形態 = Battroid mode). | 10 |
| ガウォーク | GERWALK | Intermediate (legged fighter) mode of the VF-1 Valkyrie. | 8 |
| トランス・フォーメーション | Transformation | The SDF-1 Macross's transformation from cruiser mode to its humanoid attack mode; also the title of SDF Mac... | 5 |
| デカルチャー | Deculture | Zentradi exclamation of shock/awe at human culture. | 2 |
| スペースフォールド | space fold | The Macross's fold jump (brief63187#4) / its fold system (brief63187#7). | 1 |
| ミス・マクロス | Miss Macross | The beauty contest Lynn Minmay wins (SDF Macross ep. 9). | 1 |

### Aura Battler Dunbine / The Wings of Rean

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| オーラ | aura | Life energy of Byston Well that powers aura machines; used alone in lines like オーラの力 / 悪しきオーラ / オーラ光. | 29 |
| オーラ力 | Aura Power | The aura energy of a pilot; also the name of a Dunbine-family ability that multiplies attack power for a wh... | 22 |
| オーラバトラー | Aura Battler | Class of insect-like Byston Well mecha fielded by the Drake Army and Show's side. | 16 |
| オーラバリア | Aura Barrier | Defensive field of aura machines and aura ships; Weapon 4 of the Dunbine-family units (reduces damage for a... | 7 |
| オーラノヴァ | Aura Nova | Only appears as オーラノヴァ砲, the main cannon of the aura battleship Goraon. | 6 |
| オーラマシン | Aura Machine | Collective term for all aura-powered machines (Aura Battlers, aura ships) of the Drake Army. | 6 |
| 聖戦士 | Holy Warrior | Title given to surface-world (地上人) pilots summoned to Byston Well; also part of the series title 聖戦士ダンバイン. | 6 |
| オーラシップ | Aura Ship | Aura-powered battleship; in ACE2 the description of the Gran-Garan/Goraon side ships exiled from Byston Well. | 1 |

### Heavy Metal L-Gaim

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ウィンゲルバインダー | Winger Binder | Weapon 4 of the A.Taul (Gablae's Heavy Metal): two arm-mounted binders launched by remote control. | 6 |
| バイオリレーション | Bio-Relation | Poseidal's life-energy system: heals armor (Aug's Weapon 4, akurasu); Poseidal also uses it to brainwash th... | 6 |
| バインダー | binder | Shoulder/arm weapon-pod of Heavy Metals; short for ウィンゲルバインダー / ラウンドバインダー / サーカスバインダー. | 6 |
| ヘビーメタル | Heavy Metal | Generic class name for the humanoid mecha of L-Gaim (abbr. HM). | 5 |
| バスターランチャー | Buster Launcher | L-Gaim Mk-II / Novel D.Sserd main cannon (バスターランチャー(フルパワー) = full power). | 3 |
| パワーランチャー | Power Launcher | Standard Heavy Metal launcher weapon (also ダブルパワーランチャー = Double Power Launcher). | 2 |

### Blue Comet SPT Layzner

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| SPT | SPT | Super Powered Tracer, the humanoid combat mecha of Layzner. Related classes: MF (Multi-Form) and TS (Terror... | 8 |
| V-MAX | V-MAX | The Layzner's (and Zakaal's) overdrive system: wraps the unit in a blue magnetic field for a high-speed cha... | 8 |

### Brain Powerd

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| オルファン | Orphan | Gigantic sentient alien ship buried under the Pacific; its awakening threatens Earth; base of the Reclaimers | 121 |
| プレート | plate | Orphan's disc plates sought by the Reclaimers; ALSO (crossover) inscribed plates carrying a Zentradi/Protoc... | 30 |
| ブレン | Brain | Short for Brain Powerd units (ブレンたち, ブレンパワード隊). | 28 |
| アンチボディ | Antibody | Organic mecha born from Orphan plates (Grand Chers and Brains). | 11 |
| オーガニック・エナジー | Organic Energy | The life-energy produced by Orphan and the Antibodies (Brain Powerds and Grand Chers); researched by the Is... | 6 |
| オーガニック・プレート | Organic Plate | The disc-shaped plates Orphan produces, from which Antibodies are revived. | 6 |
| チャクラ | Chakra | Brain energy in weapon names: チャクラシールド (Chakra Shield), チャクラ光 (Chakra Light), チャクラ光一斉射撃, チャクラフラッシュ. | 4 |
| オーガニック・エンジン | Organic Engine | Orphan's organic power source/engine. | 3 |
| ビー・プレート | B-Plate | The large rainbow disc plates that Orphan produces and that spawn Antibodies. Plural 'B-Plates'. | 3 |
| リバイバル | revival | Brain Powerd term for an Antibody being 'born' from an Orphan plate. | 2 |
| アンチ・ボディ | Antibody | The living organic mecha class; it includes both Brain Powerds and Grand Chers. Plural 'Antibodies'. | 1 |
| オーガニックプレート | Organic Plate | Dotless form of オーガニック・プレート (plate the Reclaimers collect). | 1 |

### Martian Successor Nadesico (TV / Prince of Darkness)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| チューリップ | Chulip | Jovian gate-ships that spawn enemy units; targets of missions like チューリップ掃討 / チューリップ排除. | 20 |
| ボソンジャンプ | Boson Jump | Teleportation/time-displacement technology of the setting | 19 |
| ゲキ・ガンガー | Gekiganger | The in-universe 1970s-style super robot anime (full title ゲキ・ガンガー3) loved by Gai Daigoji and Akito; also th... | 16 |
| グラビティブラスト | Gravity Blast | Nadesico's main gravity cannon (dotless spelling). | 11 |
| ディストーションフィールド | Distortion Field | Nadesico's gravity-wave barrier; also the Aestivalis/Nadesico-unit defensive weapon in the tutorial. | 10 |
| グラビティ・ブラスト | Gravity Blast | The Nadesico's main gravity cannon (also used by Jovian ships and the X-Aestivalis). | 1 |

### Metal Armor Dragonar

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ドラグナー | Dragonar | The three D-series prototype Metal Armors (D-1, D-2, D-3), also called D-weapons | 39 |
| メタルアーマー | Metal Armor | Humanoid combat mecha class of the series | 20 |
| マスドライバー | mass driver | Giganos Empire's lunar railgun used to launch asteroids at Earth (missions マスドライバー破壊). | 18 |
| リフター | Lifter | Atmospheric flight unit fitted to the Dragonars (ドラグナー1型(リフター装備)). | 7 |
| D兵器 | D-weapons | Collective name for the Dragonar D-series prototypes, quoted from the military manual. | 1 |

### Another Century's Episode (original)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ガーディアン | Guardian | Network of (hundreds of) orbital military satellite cannons of the Rainen Project; Gun Ark/Buster Ark can c... | 34 |
| トランスユニット | Trans Unit | Buster Ark's remote weapon pods that surround the target (Weapon 2). | 9 |
| アークシリーズ | Ark Series | UCE Design Bureau machine line: Feather Ark, Gun Ark, Buster Ark. | 7 |
| エネルギーコア | energy core | Gun Ark's power core that becomes unstable at MAX output (Op 01 story). | 6 |
| オペレーション・ライトニング | Operation Lightning | Name of the operation that covers Operations 22 and 23 (22: Defeat Death Demon Corps; 23: Escort Friendly D... | 6 |
| リミッター | limiter | Throttle limiter fitted to the Gun Ark that Marina removes (m6012#108). | 5 |
| ガーディアン・システム | Guardian System | System on the Ark-series units (Gun Ark, Buster Ark) that calls strikes from the Guardian military satellites. | 4 |

## Termos genéricos (soldados, operadores, tipos de unidade)

### Mobile Suit Gundam 0083: Stardust Memory

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| シーマ艦隊兵 | Cima Fleet Soldier | Soldier of Cima Garahau's fleet. | 2 |
| デラーズ・フリート兵 | Delaz Fleet Soldier | Rank-and-file Delaz Fleet soldier. | 2 |
| デラーズ・フリート士官 | Delaz Fleet Officer | Delaz Fleet officer. | 2 |
| 旧ジオン兵 | Ex-Zeon Soldier | Rank-and-file soldier of the former Principality of Zeon (Zeon remnants). | 2 |
| 旧ジオン士官 | Ex-Zeon Officer | Officer of the former Principality of Zeon (Zeon remnants). | 2 |

### Super Dimension Fortress Macross: Do You Remember Love?

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ゼントラーディ兵 | Zentradi Soldier | Generic Zentradi rank-and-file speaker. | 2 |
| ゼントラーディ士官 | Zentradi Officer | Generic Zentradi officer speaker. | 2 |
| ゼンドラーディ艦長 | Zentradi Captain | Generic Zentradi ship captain speaker. | 2 |
| メルトランディ兵 | Meltrandi Soldier | Generic female Zentradi (Meltrandi) soldier speaker. | 2 |

### Aura Battler Dunbine / The Wings of Rean

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ドレイク兵 | Drake Soldier | Generic enemy pilot or soldier of Drake Luft's army | 2 |
| ドレイク士官 | Drake Officer | Generic officer of Drake Luft's army | 2 |

### Heavy Metal L-Gaim

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ダバ&ギャブレー | Daba & Gablae | Joint speaker label for Daba and Gavlet speaking together (e.g. during a combination attack or a shared line). | 2 |
| ポセイダル兵 | Poseidal Soldier | Generic speaker label for a rank-and-file soldier of the Poseidal Army. | 2 |
| ポセイダル士官 | Poseidal Officer | Generic speaker label for a Poseidal Army officer. | 2 |
| 反乱軍兵 | Rebel Soldier | Generic speaker label for a soldier of the anti-Poseidal rebel army (Daba's side). | 2 |

### Brain Powerd

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| リクレイマー兵 | Reclaimer Soldier | Generic Reclaimer pilot (Grand Cher pilot) loyal to Orphan | 2 |

### Martian Successor Nadesico (TV / Prince of Darkness)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| リョーコ&ヒカル | Ryoko & Hikaru | Combined speaker label for the two pilots speaking together | 2 |
| 木連兵 | Jovian Soldier | Generic Jovian Federation soldier (speaker label) | 2 |
| 木連士官 | Jovian Officer | Generic Jovian Federation officer (speaker label) | 2 |

### Metal Armor Dragonar

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| ギガノス兵 | Giganos Soldier | Generic Giganos soldier/pilot (speaker label) | 2 |
| ギガノス士官 | Giganos Officer | Generic Giganos officer (speaker label) | 2 |

### Another Century's Episode (original)

| Japonês | Inglês | Descrição | Ocorr. |
|---|---|---|---|
| コンボ | Combo | Melee combo chain (コンボ1, コンボ2...). | 43 |
| アビリティ | Ability | Unit ability; game also writes アビリティー. | 37 |
| ダッシュ | Dash | Boost dash. | 26 |
| パージ | Purge | Detach extra armor/equipment command. | 19 |
| サブコンボ | Sub Combo | Follow-up attack after a weapon hit. | 15 |
| メモリーカード | memory card | PS2 memory card in save messages (メモリーカード(PS2)). | 15 |
| チャージ | charge | Charging a shot; in weapon names (チャージ) suffix. | 14 |
| エースポイント | Ace Points | Currency for upgrades/repairs. | 13 |
| バーニア | vernier | Boost thrust resource (バーニア消費). | 12 |
| ロックオン | lock on | Target lock (verb) / lock-on (noun). | 12 |
| フリーミッション | Free Mission | Mission replay mode. | 11 |
| モジュール | Module | Collectible item dropped in missions. | 11 |
| キャンペーン | Campaign | Story mode. | 9 |
| 新兵 | Recruit | Generic new soldier. | 9 |
| シフトメニュー | Shift Menu | Weapon-select overlay menu. | 8 |
| アラームメッセージ | Alarm message | Computer voice prefix (alarm messages in katakana-robot speech). | 6 |
| インターミッション | Intermission | Between-mission menu. | 6 |
| コマンドリスト | Command List | Pause-menu move list. | 6 |
| バーニアゲージ | vernier gauge | HUD gauge for boosting. | 6 |
| マルチロック | Multi-Lock | Lock several targets at once. | 6 |
| ローラーダッシュ | Roller Dash | Ground skating ability (Aestivalis etc.). | 6 |
| サブウェポン | sub-weapon | Secondary weapon (L1). | 4 |
| メインウェポン | main weapon | Primary weapon (□ button). | 4 |
| 工作員 | Agent | Generic covert operative/saboteur. | 3 |
| UCEオペレータ | UCE Operator | Generic UCE communications/mission operator. | 2 |
| UCE兵 | UCE Soldier | Generic UCE soldier speaker. | 2 |
| UCE士官 | UCE Officer | Generic UCE officer speaker. | 2 |
| UCE教官 | UCE Instructor | Generic UCE training instructor (exercise/tutorial missions). | 2 |
| UCE新兵 | UCE Recruit | Generic new UCE soldier. | 2 |
| UCE訓練生 | UCE Trainee | Generic UCE pilot trainee. | 2 |
| レジスタンス兵 | Resistance Soldier | Generic resistance fighter. | 2 |
| 館内放送 | PA Announcement | In-facility/ship public-address announcement used as a speaker label. | 2 |

## Decisões provisórias (use como estão)

| Japonês | Inglês | Motivo |
|---|---|---|
| ダイン | Deins | ACE3 glossary uses Stark Deins for スターク・ダイン; the plain unit must match (official Dragonar site: DEINS) |
| ＵＮＫＮＯＷＮ | UNKNOWN | fullwidth label converted to ASCII |
| クァドラン・ロー（ミリア） | Queadluun-Rau (Milia) | pilot spelled Milia (ACE3 Milia Fallyna Jenius) |
| ゲキ・ガンガー | Gekiganger | ACE3 glossary and the existing ACE2 research use Gekiganger (Wikipedia: Gekiganger III); Nadesico wiki page title is Gekigangar 3. Pendin... |
| レイ | Rei | Layzner's onboard computer (m6194 '行くぞ、レイ！'); ACE1 glossary: Rei, never confuse with Amuro Ray. hud3021 had 'Ray' (Eureka Seven, ACE3) un... |
