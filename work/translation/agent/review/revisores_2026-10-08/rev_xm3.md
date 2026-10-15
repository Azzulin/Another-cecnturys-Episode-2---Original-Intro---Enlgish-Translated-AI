# Review xm3: menu3032 - menu3057 (14 lotes, 382 rows)

Proposals: rev_xm3.json (110 rows). check_fixes.py: 0 proposed lines with errors. Every **ERRO** row of the 14 validation
reports is covered (3032:1, 3034:17, 3036:1, 3037:1, 3040:6, 3041:3, 3043_01:1, 3044:1, 3046:6, 3054:1, 3056:2, 3057:39 rows/41 errors).
Widths measured with the real menu font (merge_fill.widths); max_line_px is the provisional limit of each screen.

## Screens

- menu3032: report viewer header (List / SUBJECT / title / help text).
- menu3034: list of the Preventer / UCE Intelligence report titles (1 line, 259 px); same Japanese as the approved report titles in _fill/brief632NN.json.
- menu3036: title main menu (Campaign, Continue, Free Mission, Versus, Load, Theater) and its help lines; load confirmation.
- menu3037: Theater sound-mode select (Stereo / Dolby Pro Logic II).
- menu3040: 2P Versus menu: options, help lines, time limits, stages, space/ground unit-type notices, BGM list.
- menu3041: memory card (PS2) system messages (check, format, save, load, errors).
- menu3043: save/load slot list (headers, space needed/free, difficulty names, OPxx-MISx slot labels).
- menu3044: Versus unit select (pilot header, standby labels, button help, exit confirmation).
- menu3046: combination attack names (L2 wingman combinations), 1 line, 236 px.
- menu3054: Free Mission screen (intro text, mission/rank data labels, button help).
- menu3055: Free Mission list entries Extra 1-3 and Training 1-13 (the mission names are repeated rows filled elsewhere).
- menu3056: Free Mission victory conditions (only 3 new rows), 1 line, 261 px.
- menu3057: Free Mission secret conditions, one per mission in menu3055 order (0 = New Unit Test ... ), 253 px, 1 or 2 lines.

## Fixes

ref | JP | old EN | new EN | reason
---|---|---|---|---
**xm_menu3032_01** (1) | | | |
menu3032#7 | ここでは提出されたレポートを\n参照することができます。 | Here you can view submitted intelligence\nreports. | Here you can view\nsubmitted reports. | width (ERRO); "intelligence" was invented
**xm_menu3034_01** (24) | | | |
menu3034#1 | 未確認勢力の調査報告 | Unidentified Force Investigation Report | Unconfirmed Force Report | width (ERRO); 未確認 = unconfirmed, kept distinct from #5 所属不明勢力 "Unidentified Force"
menu3034#3 | 東京湾に出現した所属不明機 | Unidentified Unit in Tokyo Bay | Unid. Units in Tokyo Bay | width (ERRO); plural as in the approved report title "Unidentified Units in Tokyo Bay" (two units)
menu3034#4 | アンノウンの動向 | Unknown Movements | Unknown's Movements | "Unknown Movements" reads as "movements that are unknown"; the subject is the Unknown (approved title "Movements of the Unknown")
menu3034#7 | 不審衛星の分析報告 | Suspicious Satellite Analysis Report | Suspect Satellite Analysis | width (ERRO)
menu3034#10 | アルビオン命令無視 | Albion Disregards Orders | Albion Defies Orders | consistency with approved report title brief63220 "Albion Defies Orders"
menu3034#11 | デラーズ・フリート壊滅 | Delaz Fleet Destroyed | Delaz Fleet Annihilated | consistency with approved report title brief63224 "Delaz Fleet Annihilated"
menu3034#12 | ガンダム開発計画 | Gundam Development Project | Gundam Dev. Project | width (ERRO); glossary term abbreviated
menu3034#13 | 統一帝国ギガノスの動向 | United Empire of Giganos Movements | Giganos Empire Activity | width (ERRO); "United" was wrong: glossary/approved "Unified Empire of Giganos" (short form "Giganos Empire", brief63228)
menu3034#14 | ギガノス政変について | On the Giganos Coup | On the Giganos Upheaval | consistency with approved title "On the Giganos Political Upheaval" (政変)
menu3034#15 | バスターアークの性能変化について | On Buster Ark Performance Changes | Buster Ark Perf. Changes | width (ERRO)
menu3034#17 | ドレイクとシーラ・ラパーナ | Drake and Ceila Lapana | Drake and Ciela Lapana | name misspelled "Ceila": glossary Ciela Lapana (the validator passed it only via "Lapana")
menu3034#18 | ギガノス宇宙要塞稼動開始 | Giganos Space Fortress Becomes Operational | Giganos Fortress Online | width (ERRO); approved title "Giganos Space Fortress Activated" ("Space" dropped, see doubts)
menu3034#19 | 外宇宙ペンタゴナに関する報告 | Report on Outer Space Pentagona | On Deep-Space Pentagona | width (ERRO); approved title "Report on Deep Space Pentagona"
menu3034#20 | ライネンの挙兵 | Rainen Takes Up Arms | Rainen's Uprising | consistency with approved title brief63248 "Rainen's Uprising"
menu3034#22 | ドレイク軍とリクレイマー | Drake Forces and Reclaimers | Drake Army & Reclaimers | width (ERRO); approved "The Drake Army and Reclaimers"
menu3034#23 | ナデシコの配属 | Nadesico Deployment | Nadesico Assignment | 配属 = assignment (approved "Assignment of the Nadesico"), not deployment
menu3034#27 | 惑星グラドスの侵攻に関して | Regarding Planet Grados Invasion | Planet Grados Invasion | width (ERRO)
menu3034#28 | マクロスを襲撃した勢力に関して | Regarding the Force That Attacked Macross | On the Macross Attackers | width (ERRO)
menu3034#29 | グラドス地球制圧軍の動向に関して | Regarding Grados Earth Occupation Force | Grados Earth Subj. Force | width (ERRO); "Occupation" contradicted glossary "Grados Earth Subjugation Force"
menu3034#30 | ブリタイ艦潜入報告 | Vrlitwhai Ship Infiltration Report | Vrlitwhai Ship Infiltrated | width (ERRO)
menu3034#32 | ライネン私兵団所属の機体に関して | Regarding Rainen Private Army Units | Rainen Pvt. Army Units | width (ERRO)
menu3034#33 | バルクホルツ博士失踪 | Disappearance of Dr. Barkholz | Dr. Barkholz Disappears | width (ERRO)
menu3034#35 | ライネン事件に関する事後調査報告 | Post-Incident Report on Rainen Affair | Rainen Affair Follow-Up | width (ERRO); 事後調査 = follow-up investigation
menu3034#37 | ＵＣＥ防衛艦隊の壊滅 | Annihilation of UCE Defense Fleet | UCE Defense Fleet Razed | width (ERRO)
**xm_menu3036_01** (3) | | | |
menu3036#7 | 対戦 | VS Battle | Versus | 対戦 = "Versus", consistent with approved hud3013 "Versus Menu"
menu3036#13 | ２Ｐ対戦をプレイします | Play 2P VS Battle | Play a 2P Versus match | consistency: 対戦 = Versus / match (hud3013)
menu3036#15 | 音声の再生タイプを設定しムービーを鑑賞します | Configure audio playback type and watch movies | Set audio type and watch movies | width (ERRO)
**xm_menu3037_01** (1) | | | |
menu3037#3 | サウンドを変更してムービーを鑑賞します | Change sound mode and watch movies | Set sound and watch movies | width (ERRO)
**xm_menu3040_01** (12) | | | |
menu3040#0 | 対戦メニュー | VS Menu | Versus Menu | approved hud3013#49/#59 "Versus Menu"
menu3040#12 | 選択：㊤㊦　設定：㊧㊨ | Select: ㊤㊦  Set: ㊧㊨ | Select: ㊤㊦　Set: ㊧㊨ | double ASCII space (ERRO): ideographic space as in the Japanese
menu3040#14 | 対戦に使用するユニットを選択します | Select units to use in VS battle | Select units for the match | width (ERRO); 対戦 = match (hud3013 "Restart the match")
menu3040#15 | 対戦ステージを選択します | Select battle stage | Select the match stage | same term 対戦 = match on the whole screen
menu3040#16 | 対戦の制限時間を選択します | Select battle time limit | Select the match time limit | same term 対戦 = match on the whole screen
menu3040#17 | 対戦時のＢＧＭを選択します | Select battle BGM | Select the match BGM | same term 対戦 = match on the whole screen
menu3040#18 | チームに登録するユニット数を設定します | Set number of units registered to team | Set the number of units per team | width (ERRO)
menu3040#20 | コントローラのキーアサインを変更します | Change controller button configuration | Change controller key assignments | width (ERRO); キーアサイン = key assignments (menu3071/3076)
menu3040#35 | 対戦ステージに宇宙が設定されました。\n全ユニットのタイプを地上（大気圏内、\n屋内施設）対応型から宇宙対応型に変更します。 | Space selected as battle stage.\nAll unit types changed from Ground\n(Atmosphere/Indoor Facilities) to Space specs. | Space set as the match stage.\nAll units switch from Ground type\n(atmosphere/indoor) to Space type. | width (ERRO); 3 lines re-wrapped, full meaning kept
menu3040#37 | 対戦ステージに地上が設定されました。\n全ユニットのタイプを宇宙対応型から\n地上（大気圏内、屋内施設）対応型に変更します。 | Ground selected as battle stage.\nAll unit types changed from Space to\nGround (Atmosphere/Indoor Facilities) specs. | Ground set as the match stage.\nAll units switch from Space to\nGround type (atmosphere/indoor). | width (ERRO); 3 lines re-wrapped, full meaning kept
menu3040#53 | ナデシコのテーマ2 | Nadesico no Theme 2 | Nadesico Theme 2 | "Nadesico no Theme" is a half-romanization; の is a plain possessive
menu3040#66 | 我が心　明鏡止水～されどこの掌は烈火の如く | My Heart is Meikyo Shisui - Yet My Palm Burns with Raging Fire | My Heart Is Meikyo Shisui | width (ERRO); best fit, subtitle dropped (see doubts)
**xm_menu3041_01** (8) | | | |
menu3041#0 | メモリーカード差込口１のメモリーカード（ＰＳ２）をチェックしています。\n電源を切ったり、メモリーカード（ＰＳ２）を抜き差ししないでください。 | Checking Memory Card (PS2) in Memory Card Slot 1.\nDo not turn off power or remove Memory Card (PS2). | Checking Memory Card (PS2) in Slot 1.\nDo not turn off power or remove/insert the card. | width (ERRO) (2 lines max); 抜き差し = remove/insert
menu3041#2 | メモリーカード差込口１にメモリーカード（ＰＳ２）が\n差し込まれていません。\nこのゲームのセーブデータを作成するには、\n９５ＫＢ以上の空き容量がある\nメモリーカード（ＰＳ２）が必要です。\nこのままゲームをプレイしますか？ | No Memory Card (PS2) inserted in Memory Card Slot 1.\nTo create save data for this game, a Memory Card (PS2)\nwith 95 KB or more of free space is required.\nContinue playing game without saving? | No Memory Card (PS2) inserted in Memory Card Slot 1.\nTo create save data for this game, a Memory Card (PS2)\nwith 95 KB or more of free space is required.\nContinue playing the game without saving? | grammar ("playing game"); auto-rewrap fits 487 px
menu3041#4 | メモリーカード差込口１のメモリーカード（ＰＳ２）の\n空き容量が不足しています。\nこのゲームのセーブデータを作成するには、\n９５ＫＢ以上の空き容量がある\nメモリーカード（ＰＳ２）が必要です。\nこのままゲームをプレイしますか？ | Insufficient free space on Memory Card (PS2) in Slot 1.\nTo create save data for this game, a Memory Card (PS2)\nwith 95 KB or more of free space is required.\nContinue playing game without saving? | Insufficient free space on Memory Card (PS2) in Slot 1.\nTo create save data for this game, a Memory Card (PS2)\nwith 95 KB or more of free space is required.\nContinue playing the game without saving? | grammar ("playing game"); auto-rewrap fits 487 px
menu3041#13 | Ｎｏ．00 にセーブデータを上書きします。\nよろしいですか？ | Overwrite save data to No. 00?\nAre you sure? | Overwrite the save data in No. 00?\nAre you sure? | "overwrite ... to" was the wrong preposition
menu3041#14 | ㍉セーブ成功確認 | ㍉Save Confirmation | ㍉Save Successful | 成功確認 = success notice; was identical to #21 セーブ確認
menu3041#19 | メモリーカード差込口１のメモリーカード（ＰＳ２）にセーブしています。\n電源を切ったり、メモリーカード（ＰＳ２）を抜き差ししないでください。 | Saving to Memory Card (PS2) in Memory Card Slot 1.\nDo not turn off power or remove Memory Card (PS2). | Saving to Memory Card (PS2) in Slot 1.\nDo not turn off power or remove/insert the card. | width (ERRO) (2 lines max); 抜き差し = remove/insert
menu3041#26 | ㍉ロード成功確認 | ㍉Load Confirmation | ㍉Load Successful | 成功確認 = success notice; was identical to menu3036#0 ロード確認
menu3041#29 | メモリーカード差込口１のメモリーカード（ＰＳ２）からロードしています。\n電源を切ったり、メモリーカード（ＰＳ２）を抜き差ししないでください。 | Loading from Memory Card (PS2) in Memory Card Slot 1.\nDo not turn off power or remove Memory Card (PS2). | Loading from Memory Card (PS2) in Slot 1.\nDo not turn off power or remove/insert the card. | width (ERRO) (2 lines max); 抜き差し = remove/insert
**xm_menu3043_01** (2) | | | |
menu3043#9 | 必要容量：９５ＫＢ以上 | Required Space: 95 KB or more | Space Needed: 95 KB or more | width (ERRO)
menu3043#11 | 新規作成 | New Game | New Save | 新規作成 on the save-slot screen = create new save data, not "New Game"
**xm_menu3044_01** (3) | | | |
menu3044#7 | タイトル選択：㊤㊦　ユニット選択：㊧㊨　取消し：△　切替：□　決定：○　戻る：× | Select Title: ㊤㊦ Select Unit: ㊧㊨ Cancel: △ Switch: □ Confirm: ○ Back: × | Title: ㊤㊦　Unit: ㊧㊨　Cancel: △　Switch: □　OK: ○　Back: × | width (ERRO); 決定 = OK as in approved common.json/hud3013; ideographic spaces
menu3044#9 | ㍉対戦確認 | ㍉VS Battle Confirmation | ㍉Versus Confirmation | 対戦 = Versus
menu3044#10 | ユニット選択を終了して、\n対戦メニューに戻ります。\nよろしいですか？ | Exit unit select and return\nto VS menu?\nAre you sure? | End unit selection and return\nto the Versus Menu.\nAre you sure? | Versus Menu (hud3013); the JP is a statement + "Are you sure?", not a double question
**xm_menu3046_01** (7) | | | |
menu3046#1 | バスターライフル＆フルオープン | Buster Rifle & Full Open | B. Rifle & Full Open | width (ERRO)
menu3046#3 | バスターライフル＆メガキャノン | Buster Rifle & Mega Cannon | B. Rifle & Mega Cannon | width (ERRO)
menu3046#8 | ランチャーコンビネーションⅡ | Launcher Combination II | Launcher Comb. II | width (ERRO); "Combo" avoided (glossary: Combo = melee chain)
menu3046#9 | バスターランチャー（フルパワー） | Buster Launcher (Full Power) | B. Launcher (Full Pwr) | width (ERRO)
menu3046#18 | ダブルゲキガンフレア | Double Geki-Gan Flare | Double Gekigan Flare | Gekigan (glossary Gekiganger), not "Geki-Gan"
menu3046#20 | 砲戦フォーメーションアタック | Artillery Formation Attack | Artillery Form. Attack | width (ERRO)
menu3046#21 | カスタムフォーメーションアタック | Custom Formation Attack | Custom Form. Attack | width (ERRO)
**xm_menu3054_01** (1) | | | |
menu3054#27 | 選択：㊤㊦　設定：㊧㊨　ミッションスキップ：⑤／① | Select: ㊤㊦  Set: ㊧㊨  Skip Mission: ⑤/① | Select: ㊤㊦　Set: ㊧㊨　Skip: ⑤/① | double ASCII space + width (ERRO); "Skip" follows the approved hud3013 "Page: ①/⑤" precedent
**xm_menu3056_01** (3) | | | |
menu3056#7 | チューリップを１０機以上破壊 | Destroy 10 or more Tulips | Destroy 10+ Chulips | glossary Chulip (was "Tulips") + width
menu3056#59 | 敵機を1００機以上撃破 | Destroy 100 or more enemy units | Destroy 100+ enemy units | width (ERRO)
menu3056#72 | ガンダムデスサイズらに勝利 | Defeat Gundam Deathscythe and others | Defeat Deathscythe & Co. | width (ERRO)
**xm_menu3057_01** (45) | | | |
menu3057#1 | ダインを全滅させる | Wipe out all Dyne units | Wipe out all Deins | glossary ダイン = Deins (ERRO)
menu3057#4 | クインシィ・グランチャーと同時に\n出現するグランチャーを全滅させる | Wipe out all Grandchers appearing alongside Quincy Grandcher | Wipe out the Grand Chers\nthat appear with Quincy | width (ERRO); glossary Grand Cher (was "Grandcher"); "Quincy" = the pilot of the Quincy Grand Cher
menu3057#5 | グランチャーを全滅させる | Wipe out all Grandchers | Wipe out all Grand Chers | glossary Grand Cher (was "Grandchers")
menu3057#7 | チューリップを全滅させる | Wipe out all Tulips | Wipe out all Chulips | glossary Chulip (was "Tulips")
menu3057#9 | ６０秒以内に１５機以上を撃破し、\n増援のダウツェンを全滅させる | Destroy 15 or more units within 60 seconds and wipe out reinforcing Dowtwens | Destroy 15+ in 60s, then\nall reinforcing Dowtwens | width (ERRO)
menu3057#10 | 敵艦の搭載するドラッツェ\nおよびゲルググＭを全滅させる | Wipe out Dra-Cs and Gelgoog Ms carried by enemy ships | Destroy all enemy ships'\nDra-Cs/Gelgoog Marines | width (ERRO); glossary Gelgoog Marine (was "Gelgoog Ms")
menu3057#11 | フンボルトを撃破し、アルビオンが\nノーダメージの状態でクリアする | Destroy the Humboldt and clear with Albion taking no damage | Destroy the Humboldt\nwith no Albion damage | width (ERRO); "clear" is implicit in a secret condition
menu3057#12 | ゲルググＭの領域離脱を\n完全に阻止する | Completely prevent Gelgoog Ms from leaving the combat zone | Fully prevent Gelgoog\nMarines leaving the area | width (ERRO); glossary Gelgoog Marine
menu3057#13 | ザクⅡを全滅させる | Wipe out all Zaku II units | Wipe out all Zaku IIs | width (ERRO)
menu3057#20 | １２０秒以内にクラビウスを破壊して\nギガノス軍を撃退する | Destroy Clavius and repel Giganos forces within 120 seconds | Destroy Clavius in 120s\nand repel Giganos forces | width (ERRO)
menu3057#21 | ８０秒以内に\nチューリップを７機以上破壊する | Destroy 7 or more Tulips within 80 seconds | Destroy 7+ Chulips\nwithin 80 seconds | glossary Chulip (was "Tulips")
menu3057#22 | １８０秒以内に戦力値を半減させ、\n増援のナムワンを全滅させる | Reduce enemy battle strength by half within 180 seconds and wipe out reinforcing Namwans | Halve foe power in 180s,\ndestroy Namwan backup | width (ERRO); 戦力値 compressed to "foe power", 増援 = backup (see doubts)
menu3057#23 | アキト、ガイが出現してから\n４５秒以内に撤退させる | Force Akito and Gai to retreat within 45 seconds of appearing | Force Akito and Gai out\nwithin 45s of appearing | width (ERRO)
menu3057#24 | 全てのソーラー施設を破壊し、\nグン･ジェム隊を全て撃破する | Destroy all solar facilities and defeat all of Gun Jem Squad | Wreck all solar facilities\n& all of Gon Jem Squad | width (ERRO); glossary Gon Jem Squad (was "Gun Jem")
menu3057#25 | 全てのランチゲートを破壊し、\nグン･ジェム隊を全て撃破する | Destroy all launch gates and defeat all of Gun Jem Squad | Destroy all launch gates\n& all of Gon Jem Squad | width (ERRO); glossary Gon Jem Squad (was "Gun Jem")
menu3057#26 | 浮遊砲台を全滅させる | Wipe out all floating gun turrets | Wipe out floating turrets | width (ERRO)
menu3057#27 | 宇宙高速艦を全滅させる | Wipe out all space high-speed craft | Wipe out fast space ships | width (ERRO); 艦 = ships, not "craft"
menu3057#28 | １００秒以内に、ギガノス軍の\n敵ユニットを３０機以上撃破する | Destroy 30 or more Giganos enemy units within 100 seconds | Within 100s, destroy 30+\nGiganos units | width (ERRO)
menu3057#29 | 要塞東部の格納庫に侵入し、\n全ての敵機を破壊する | Infiltrate fortress eastern hangar and destroy all enemy units | Infiltrate the east hangar\nand destroy all enemies | width (ERRO) ("fortress" implied by the mission, see doubts)
menu3057#30 | エルガイムを一度も誤射せず\nミッションを達成する | Clear mission without hitting L-Gaim once with friendly fire | Clear the mission without\never hitting the L-Gaim | width (ERRO)
menu3057#32 | シェルストロームの\n全ての部位を破壊する | Destroy all parts of the Schaelstorm | Destroy all parts of\nthe Shell Storm | approved spelling Shell Storm (m6143#0), not "Schaelstorm"
menu3057#34 | 主砲ユニットを破壊する前に、\n防空基地の破壊率を１００％にする | Achieve 100％ destruction of anti-air base before destroying main cannon unit | Raze the air defense base\nbefore the main cannon | width (ERRO); "Raze" = 100％ destruction rate
menu3057#36 | ナナフシの攻撃を被弾せず、\n１８０秒以内に施設を全滅させる | Clear all facilities within 180 seconds without taking hits from Nanafushi | Take no Nanafushi hits,\nwipe out facilities in 180s | width (ERRO); "Clear all facilities" was ambiguous (全滅 = destroy)
menu3057#37 | ナナフシの攻撃を被弾せず、\n９０秒以内にナナフシを破壊する | Destroy Nanafushi within 90 seconds without taking hits from Nanafushi | Take no Nanafushi hits,\ndestroy it within 90s | width (ERRO)
menu3057#39 | アーミー・グランチャーを\n２０機以上撃破する | Destroy 20 or more Army Grandchers | Destroy 20 or more\nArmy Grand Chers | glossary Army Grand Cher (was "Grandchers")
menu3057#40 | デビルエステバリスを全滅させる | Wipe out all Devil Aestivalis units | Wipe out Devil Aestivalis | width (ERRO)
menu3057#45 | バッタを５０機以上撃破する | Destroy 50 or more Batta units | Destroy 50 or more Batta | width (ERRO)
menu3057#46 | ブレイバーおよび\nディマージュを全滅させる | Wipe out all Bravers and Dimages | Wipe out all Bravers\nand Dimarges | glossary Dimarge (ERRO)
menu3057#47 | 敵戦艦の搭載機を全滅させる | Wipe out all carrier craft from enemy battleships | Destroy battleships' units | width (ERRO); "carrier craft" misread 搭載機 (units carried aboard) (see doubts)
menu3057#48 | 重攻撃機を１０機以上撃破する | Destroy 10 or more heavy attack aircraft | Kill 10+ heavy attackers | width (ERRO); 重攻撃機 = heavy attackers as approved in m6211
menu3057#49 | 重攻撃機を全滅させる | Wipe out all heavy attack aircraft | Wipe out heavy attackers | width (ERRO); heavy attackers (m6211)
menu3057#50 | 破壊率を２０％以下に抑える | Keep destruction rate at 20％ or below | Destruction rate: 20％ max | width (ERRO); approved term Destruction Rate
menu3057#51 | 敵艦を８隻以上撃破する | Destroy 8 or more enemy ships | Destroy 8+ enemy ships | width (ERRO)
menu3057#52 | ヌージャデル・ガーおよび\nグラージを７０機以上撃破する | Destroy 70 or more Noupzachet-Gers and Glaugs | Destroy 70+ Glaugs and\nNousjadeul-Gers | width (ERRO); glossary Nousjadeul-Ger (ERRO)
menu3057#53 | 死鬼隊を全滅させる | Wipe out all of Death Demon Squad | Wipe out all Shikitai | width (ERRO); 死鬼隊 = Shikitai as approved (brief63021, m6221)
menu3057#55 | チェインを２４０秒以上つなぐ | Maintain chain for 240 seconds or longer | Keep a chain for 240s+ | width (ERRO)
menu3057#56 | 全ての友軍艦が領域を離脱する | All friendly ships leave the combat zone | All allied ships exit area | width (ERRO); 友軍艦 = Allied Ship (hud3013)
menu3057#57 | １２０秒以内にスラッシュを\n１２隻以上撃破する | Destroy 12 or more Thrash ships within 120 seconds | Destroy 12+ Thrash ships\nwithin 120 seconds | width (ERRO)
menu3057#58 | 明鏡止水モードで\nデビルガンダムにとどめを刺す | Deliver finishing blow to Devil Gundam in Meikyo Shisui Mode | Finish off Devil Gundam\nin Meikyo Shisui Mode | width (ERRO)
menu3057#63 | ２５０秒以内に\nノヴィス・ノアが領域を離脱する | Novis Noah leaves the combat zone within 250 seconds | Novis Noah exits the area\nwithin 250 seconds | width (ERRO)
menu3057#64 | ３０秒以内に\nバロンズゥを巨大化させる | Cause Baronzwo to enlarge within 30 seconds | Make Baronz grow giant\nwithin 30 seconds | glossary Baronz (was "Baronzwo")
menu3057#65 | 敵機を５０機以上撃破する | Destroy 50 or more enemy units | Destroy 50+ enemy units | width (ERRO)
menu3057#67 | 敵艦を１５隻以上撃破する | Destroy 15 or more enemy ships | Destroy 15+ enemy ships | width (ERRO)
menu3057#68 | 空戦ポッドと重攻撃機を\n計３０機以上撃破する | Destroy 30 or more aerial pods and heavy attack craft combined | Destroy 30+ Aerial Pods\nand heavy attackers total | width (ERRO); Aerial Pod (menu3062) / heavy attackers (m6211)
menu3057#69 | ６０秒以内にヌージャデル・ガーを\n１５機以上撃破する | Destroy 15 or more Noupzachet-Gers within 60 seconds | Within 60s, destroy 15+\nNousjadeul-Gers | width (ERRO); glossary Nousjadeul-Ger (ERRO)

## Recurring labels (JP -> EN) settled here

| JP | EN | source |
|---|---|---|
| 選択：㊤㊦ | Select: ㊤㊦ | hud3013 |
| 設定：㊧㊨ | Set: ㊧㊨ | |
| 決定：○ | OK: ○ | common.json#7, hud3013#24 (not "Confirm") |
| 戻る：× | Back: × | hud3013#25 |
| 取消し：△ / 切替：□ | Cancel: △ / Switch: □ | |
| タイトル選択 / ユニット選択 (button help) | Title / Unit | width (menu3044#7) |
| ミッションスキップ：⑤／① | Skip: ⑤/① | like hud3013 "Page: ①/⑤" |
| item separator in button help | 　 (ideographic space) | never two ASCII spaces |
| ㍉…確認 (dialog title) | ㍉... Confirmation | ㍉確認 alone = ㍉Confirm (hud3013#41) |
| ㍉…成功確認 | ㍉Save Successful / ㍉Load Successful | |
| 対戦 (mode/menu) | Versus; 対戦メニュー = Versus Menu | hud3013#49/#59 |
| 対戦 (in a sentence) | match | hud3013#58/#60 |
| キャンペーン / フリーミッション | Campaign / Free Mission | GLOSSARIO |
| 編入 | admit / Admission | menu3013 |
| 演習N | Training N | menu3004#12 |
| メモリーカード（ＰＳ２） / 差込口１ | Memory Card (PS2) / (Memory Card) Slot 1 | |
| 新規作成 (save list) | New Save | |
| 難易度 | Difficulty | |
| コンビネーション | Combination (never "Combo") | GLOSSARIO Combo = melee chain |
| …の動向 (report titles) | ... Movements | brief632NN |
| 所属不明 / 未確認 / アンノウン | Unidentified (Unid.) / Unconfirmed / Unknown | |
| チューリップ | Chulip | GLOSSARIO |
| 重攻撃機 / 空戦ポッド | heavy attacker / Aerial Pod | m6211 / menu3062 |
| 死鬼隊 | Shikitai | brief63021, m6221 |
| シェルストローム | Shell Storm | m6143#0 |
| 破壊率 | Destruction Rate | m6151, brief63098 |
| 友軍艦 | allied ship | hud3013#42 |
| N機以上撃破 (1-line conditions) | Destroy N+ ... ("N or more" where it fits) | |
| N秒以内に (tight rows) | in/within Ns; "within N seconds" where it fits | |

## Doubts not changed (for the project owner)

1. **Provisional widths force abbreviations.** Many rows are best fits for the provisional max_line_px and should be re-expanded once the boxes are measured:
   menu3034 (#3 "Unid. Units in Tokyo Bay", #12 "Gundam Dev. Project", #15 "Perf.", #18 "Giganos Fortress Online" drops "Space", #29 "Grados Earth Subj. Force", #32 "Pvt."; the approved report titles in brief632NN are the full forms);
   menu3046 (#1/#3 "B. Rifle", #8 "Launcher Comb. II", #9 "B. Launcher (Full Pwr)", #20/#21 "Form. Attack"; full forms: Buster Rifle & Full Open, Buster Rifle & Mega Cannon, Launcher Combination II, Buster Launcher (Full Power), Artillery/Custom Formation Attack);
   menu3054#27 "Skip: ⑤/①" (full: "Skip Mission: ⑤/①", 387 px > 365).
2. **menu3040#66** (BGM title 我が心　明鏡止水～されどこの掌は烈火の如く): only "My Heart Is Meikyo Shisui" fits 350 px on one line; the subtitle ("Yet This Palm Burns Like a Raging Fire") is cut. Full form when the box allows: "My Heart Is Meikyo Shisui - Yet This Palm Burns Like Raging Fire".
3. **menu3057 (253 px, about 24 characters a line)**: rows compressed with small meaning loss: #22 戦力値を半減 = "Halve foe power" (approved term is "war potential") and "destroy Namwan backup" drops 全滅's "all"; #29 drops "fortress" (要塞東部 = the fortress's east hangar); #47 敵戦艦の搭載機 = "Destroy battleships' units" drops "enemy"/"all"; #48 "Kill 10+ heavy attackers" ("Destroy" does not fit); #11 drops the explicit "clear" (implicit in a secret condition); #9 "then all reinforcing Dowtwens" is elliptical (verb carried from "Destroy"). The secret-condition panel probably equals the victory-condition box: note that repeated rows already filled in menu3056 (e.g. #8 "Destroy at least 20 enemy units", about 312 px) exceed 261 px, so the real box is likely wider.
4. **Count/time style**: approved missions use both "Destroy at least 20 enemy units" (m6042) and "Destroy 12 or more solar facilities" (m6111). I used "N or more" where it fits and "N+" / "Ns" only where it does not; warning-only rows (auto-rewrap) were left as delivered ("within 240 seconds" etc.).
5. **menu3041 Ｎｏ．00 (#13, #22)**: the halfwidth "00" is probably overwritten by the game with the slot number. If the game writes it at a fixed byte offset, any English text before "No. 00" breaks it. Please confirm in the emulator (not a token, so the validator does not check it).
6. **menu3037#2** ＤｏｌｂｙＤｉｇｉｔａｌＰｒｏＬｏｇｉｃⅡ: kept the real trademark "Dolby Pro Logic II" (the Japanese says "Dolby Digital ProLogic II", which is not a real Dolby product). "Dolby Digital Pro Logic II" fits (254 px) if literal fidelity is preferred.
7. **menu3040 BGM titles**: the translator romanized the Japanese titles (Dunbine Tobu, Melos no You ni, Semarikurumono e, Tatakai no Unmei, Soukougeki, Ai Oboete Imasu ka) and translated others; I kept that policy. #40 聖戦士たち "Seisenshitachi" triggers the glossary warning (聖戦士 = Holy Warrior); "Holy Warriors" is the alternative. #43 could be spaced "Semarikuru Mono e".
8. **menu3057 names without glossary entry** kept from the translator / other menus: Nutria (approved m6032), Humboldt, Namwan, Thrash, Yanma (as in the menu3063 return), Clavius, SD-04, picket ships; 宇宙高速艦 "fast space ships" and 浮遊砲台 "floating turrets" may be specific enemy class names (check menu3062/3063 when reviewed). スラッシュ is counted with 隻 (ships) in #57.
9. **menu3057#4**: クインシィ・グランチャー written as "Quincy" (her Grand Cher) to fit; full: "Wipe out the Grand Chers that appear with Quincy Grand Cher".
10. **menu3041#0/#19/#29**: "Memory Card Slot 1" shortened to "Slot 1" (the translator already did so in #4/#11/#20/#25); 抜き差し rendered "remove/insert the card". Row #18 (3 lines, auto-rewrap) still says "remove Memory Card (PS2)"; left as is.
11. **menu3043#13/#15 and menu3054#10-14**: ルーキー/パイロット/リーダー/ベテラン/エース translated Rookie/Pilot/Leader/Veteran/Ace as delivered; whether these are difficulty levels or clear ranks is not clear from the table alone.
12. **menu3036#11** "Resume gameplay from save" and **menu3054#17** "Unachieved" kept (merely different; "Continue from where you left off" / "Not Achieved" are alternatives).
