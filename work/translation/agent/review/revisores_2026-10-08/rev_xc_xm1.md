# Meaning review: xc (flashbacks m6320-m6325) + menus menu3000/3001/3002/3004/3009/3013/3018

Proposals: `rev_xc_xm1.json` (92 rows; `check_fixes.py`: 0 proposed lines with errors). Every **ERRO** row of the 11
validation reports is covered. BASE_RULES.md was not available on this machine; PLANO.md and the task rules were used.

Rows reviewed: xc_01 80, xc_02 41, menu3000 77, menu3001 36, menu3002 13, menu3004 31, menu3009 13,
menu3013 80+80+20, menu3018 53 (total 524).

## What each menu screen is (for the docs)

- **menu3000**: list of playable unit names (unit select / Free Mission roster), with variant and terrain suffixes
  (：地上専用 / ：宇宙専用). One line, 332 px.
- **menu3001**: mission result screen (MISSION CLEAR): clear time, kill points, damage, chain time, operation rating,
  Ace Points earned, unit EXP, wingman proficiency, module obtained, pilot rank (SS-E and #i...#i rank titles), save prompt.
- **menu3002**: module names (equipped-module slot list, Recovery/Support Kit-Tool-Device, Afterburner...). 146 px.
- **menu3004**: Intermission main menu: status labels (Ace Points, Units, Missions Cleared), menu items (Sortie, Viewer,
  Encyclopedia, Comm Log, Report, Training, Save, Options), their help lines, the training-field choice and the help page.
- **menu3009**: Viewer (unit model gallery): player/other unit categories, viewer button help, help page.
- **menu3013**: Sortie Select (pre-mission) screen: player/wingman unit selection, Unit Upgrade (stats, special upgrade,
  evolution), Module equip, Unit Admission, Emergency Repair, all confirmations/warnings and help pages.
- **menu3018**: Encyclopedia index (entry titles: factions, organizations, people, mecha classes, terms). 231 px.

## Most serious problems found

1. m6322#13: wrong speaker. The previous row (repeat #12) is Tak calling "Marina!", so 大丈夫！ is Marina's "I'm fine!";
   EN had Tak's "Hang in there!".
2. m6324#20: wrong referent. Tak teases Marina that she was aiming at him; EN said "They were clearly aiming at me".
3. m6322#15: Marina's trailing-off line became an invented statement ("I never wanted to do this").
4. m6322#4-5: split sentence closed in the first row; m6323#6 母艦 rendered "flagship".
5. Glossary names that passed the validator only as substrings or single words: GP02A, Yatenkou, Jovian Union (木連),
   Allied Space Forces (連合宇宙軍), Gradosian Empire, United Empire of Giganos, plus the hard errors Bull Gren,
   Oukaoh, Confeito.
6. All button-help lines used single ASCII spaces (or double, in menu3013) instead of the ideographic space of the JP.
7. menu3013#108/#119: forbidden ＝.

## Fixes (ref | JP | old EN | new EN | reason)

### xc_01 (13 fixes)

- m6321#4 | <on()><sp(20)>…いえ。戦時中ですから…\n兵員が足りない以上、当然の仕事です。<ab(0)><off()> | <on()><sp(20)>...No. We are at war...\nIf we're short-handed, it's my duty.<ab(0)><off()> | <on()><sp(20)>...Not at all. We are at war...\nWe're short-handed, so it's my duty.<ab(0)><off()> | いえ = modest "Not at all", not a flat "No"; 以上 = since/given that, not a hypothetical "If"
- m6321#12 | <on()><sp(20)>う…遅くなりました！　援軍です！<ab(0)><off()> | <on()><sp(20)>Sorry I'm late!\nReinforcements are here!<ab(0)><off()> | <on()><sp(20)>Ugh... Sorry we're late!\nReinforcements are here!<ab(0)><off()> | restores the dropped う... and the subject: Tak arrives with others (お前たち / 自分たち in #13-14), so "we're late"
- m6321#21 | <on()><sp(20)>…\nタックと言ったわよね…少し…見直した。<ab(0)><off()> | <on()><sp(20)>...Your name was Tak, right?\nI think a little higher of you now.<ab(0)><off()> | <on()><sp(20)>...Your name was Tak, right?\nI think... a little better of you now.<ab(0)><off()> | "think higher of" is not idiomatic; keeps the 少し... pause
- m6322#4 | <on()><sp(20)>…功績と命令違反の数が同じくらいで、\nおまけに極度の機械音痴が小隊長なんて、<ab(0)> | <on()><sp(20)>...Equal merits and order violations,\nand completely inept with machines...<ab(0)> | <on()><sp(20)>...A guy with as many merits as order\nviolations, and hopeless with machines,<ab(0)> | JP sentence continues into #5 (subject clause here, 世も末ね there) but EN closed it; now one sentence across #4-#5
- m6322#5 | <sp(20)>世も末ね。<ab(0)><off()> | <sp(20)>It's the end of the world.<ab(0)><off()> | <sp(20)>as our platoon leader?\nWhat's the world coming to?<ab(0)><off()> | lowercase continuation of #4; 世も末ね = "What's the world coming to?"
- m6322#6 | <on()><sp(20)>…パイロットの癖にすぐ乗り物に酔う\n誰かさんよりは、適任だと思うがな？<ab(0)> | <on()><sp(20)>...I'm more qualified than someone\nwho gets motion-sick as a pilot.<ab(0)> | <on()><sp(20)>...I'm better suited than a certain\npilot who gets motion-sick so easily.<ab(0)> | restores すぐ (so easily) and the ironic 誰かさん ("a certain pilot"); "motion-sick as a pilot" was ambiguous
- m6322#13 | <on()><sp(20)>大丈夫！<ab(0)><off()> | <on()><sp(20)>Hang in there!<ab(0)><off()> | <on()><sp(20)>I'm fine!<ab(0)><off()> | WRONG SPEAKER: #12 (repeated row, not in the lote) is Tak's "マリナ！", so 大丈夫！ is Marina answering "I'm fine!", not Tak's "Hang in there!"
- m6322#14 | <on()><sp(20)>堅くなるな。\n訓練じゃ俺より成績良かったんだろ？<ab(0)><off()> | <on()><sp(20)>Don't tense up.\nYou scored better than me in training!<ab(0)><off()> | <on()><sp(20)>Don't tense up. You outscored\nme in training, didn't you?<ab(0)><off()> | JP is a question tag (んだろ？); EN had made it an exclamation
- m6322#15 | <on()><sp(20)>訓練と実戦は違う…！\n本当はこんなこと…<ab(0)><off()> | <on()><sp(20)>Training and combat are different...!\nI never wanted to do this...<ab(0)><off()> | <on()><sp(20)>Training and combat are different...!\nThe truth is, this kind of thing...<ab(0)><off()> | hedge turned into fact: Marina trails off (本当はこんなこと…) and Tak completes it in #16; "I never wanted to do this" was invented
- m6322#17 | <on()><sp(20)>でも…守るためには…\n今は、戦うしかないのよ…！<ab(0)><off()> | <on()><sp(20)>But... in order to protect...\nwe have to fight right now...!<ab(0)><off()> | <on()><sp(20)>But... in order to protect...\nall we can do for now is fight...!<ab(0)><off()> | 今は = for now (the only option for the time being), not "right now"
- m6323#2 | <on()><sp(20)>私は平気。\nタック、復帰したばかりなのに…<ab(0)><off()> | <on()><sp(20)>I'm fine.\nTak, and you only just returned...<ab(0)><off()> | <on()><sp(20)>I'm fine.\nTak, you've only just come back...<ab(0)><off()> | "Tak, and you only just returned" was ungrammatical
- m6323#6 | <sp(20)>あなたは９時方向から、\n回りこんで母艦に向かって。<ab(0)><off()> | <sp(20)>Flank around from nine o'clock\nand head for the flagship.<ab(0)><off()> | <sp(20)>You circle around from nine o'clock\nand head for the mothership.<ab(0)><off()> | 母艦 = mothership/carrier, not flagship (旗艦); restores the contrastive あなたは
- m6323#8 | <on()><sp(20)>…冷静な判断の結果よ。\nこの機体では邪魔になる…<ab(0)> | <on()><sp(20)>...It's calm judgment.\nThis unit will only get in the way...<ab(0)> | <on()><sp(20)>...It's the result of calm judgment.\nIn this unit, I'd only be a burden...<ab(0)> | この機体では邪魔になる = in this unit SHE would be in the way (EN said the unit gets in the way); 冷静な判断の結果 rendered in full (Tak echoes "calm judgment" in #11)

### xc_02 (4 fixes)

- m6324#20 | <on()><sp(20)>明らかに俺を狙ってただろ…？<ab(0)><off()> | <on()><sp(20)>They were clearly aiming right\nat me back then, weren't they...?<ab(0)><off()> | <on()><sp(20)>You were obviously aiming right\nat me back then, weren't you...?<ab(0)><off()> | WRONG REFERENT: Tak teases Marina that SHE was aiming at him (she answers "I only saved you" in #21; cf. m6320#13-16); EN said "They were..."
- m6325#3 | <on()><sp(20)>明日からはよろしく頼んだよ。<ab(0)><off()> | <on()><sp(20)>I'll be counting on you tomorrow.<ab(0)><off()> | <on()><sp(20)>Starting tomorrow,\nI'm counting on you.<ab(0)><off()> | 明日から = starting tomorrow (from now on), not just "tomorrow"
- m6325#6 | <on()><sp(20)>…その代わり…私達のどちらかが、\n死ぬことになるんでしょう…。 | <on()><sp(20)>...And in return... one of us\nwill have to die, won't we... | <on()><sp(20)>...But in return... one of us is\ngoing to die. Isn't that right...? | "one of us will have to die, won't we" was an ungrammatical tag; その代わり = but in return
- m6325#11 | <on()><sp(20)>…タックには、言わないと約束して。\n犠牲になるのは…私だけでいい。<ab(0)><off()> | <on()><sp(20)>...Promise you won't tell Tak.\nI'll be the only sacrifice.<ab(0)><off()> | <on()><sp(20)>...Promise you won't tell Tak.\nLet me be... the only one sacrificed.<ab(0)><off()> | restores the pause and 私だけでいい ("let it be only me"); "I'll be the only sacrifice" lost the nuance

### xm_menu3000_01 (25 fixes)

- menu3000#4 | ガンダム試作２号機 | Gundam GP02A | Gundam GP02 | glossary: ガンダム試作2号機 = Gundam GP02 (the "A" is not in the JP; it passed the validator only as a substring)
- menu3000#20 | ウィングキャリバー | Wing Calibur | Wing Caliber | standard romanization of Billbine's flight form is "Wing Caliber" (not in the glossary; see doubts)
- menu3000#21 | ビルバイン 迷彩カラー | Billbine Camouflage Color | Billbine (Camouflage) | glossary: ビルバイン迷彩カラー = Billbine (Camouflage)
- menu3000#22 | ウィングキャリバー 迷彩カラー | Wing Calibur Camouflage Color | Wing Caliber (Camouflage) | same pattern as #21 + Wing Caliber spelling
- menu3000#37 | ドラグナー３型（後期型） | Dragonar-3 (Late Type) | Dragonar-3 (Late Model) | glossary: ドラグナー3型(後期型) = Dragonar-3 (Late Model)
- menu3000#38 | ドラグナー１型（リフター装備）：地上専用 | Dragonar-1 (Lifter Equipped): Ground Only | Dragonar-1 (Lifter): Ground Only | ERRO width 422>332; "(Lifter)" keeps the equipment meaning
- menu3000#39 | ドラグナー１型（キャバリアー装備）：宇宙専用 | Dragonar-1 (Cavalier Equipped): Space Only | Dragonar-1 (Cavalier): Space Only | ERRO width 429>332
- menu3000#41 | ドラグナー２型（リフター装備）：地上専用 | Dragonar-2 (Lifter Equipped): Ground Only | Dragonar-2 (Lifter): Ground Only | ERRO width 423>332
- menu3000#43 | ドラグナー３型（リフター装備）：地上専用 | Dragonar-3 (Lifter Equipped): Ground Only | Dragonar-3 (Lifter): Ground Only | ERRO width 423>332
- menu3000#48 | 高機動型ブラックサレナ | High Mobility Black Sarena | Hi-Mob. Black Sarena | glossary: 高機動型ブラックサレナ = Hi-Mob. Black Sarena (same JP must read the same on every screen)
- menu3000#50 | エステバリスＣ（リョーコ） | Aestivalis Custom (Ryoko) | Aestivalis C (Ryoko) | glossary: エステバリスC(リョーコ) = Aestivalis C (Ryoko)
- menu3000#51 | エステバリスＣ（ヒカル） | Aestivalis Custom (Hikaru) | Aestivalis C (Hikaru) | glossary: Aestivalis C (Hikaru)
- menu3000#52 | エステバリスＣ（イズミ） | Aestivalis Custom (Izumi) | Aestivalis C (Izumi) | glossary: Aestivalis C (Izumi)
- menu3000#54 | 夜天光 | Yatenkou | Yatenko | glossary: 夜天光 = Yatenko ("Yatenkou" passed only as a substring)
- menu3000#67 | レイズナーMk－Ⅱ・企画版（飛行形態） | Layzner Mk-II Concept Ver. (Flight Mode) | Layzner Mk-II Concept (Flight) | ERRO width 405>332; best fit (see doubts)
- menu3000#69 | 強化型レイズナー グレネードランチャー | Enhanced Layzner Grenade Launcher | Enh. Layzner Grenade Launcher | ERRO width 367>332; Enh. = 強化型
- menu3000#70 | 強化型レイズナー フレイムランチャー | Enhanced Layzner Flame Launcher | Enh. Layzner Flame Launcher | ERRO width 346>332; Enh. for consistency with #69/#71
- menu3000#71 | 強化型レイズナー ウイングユニット：地上専用 | Enhanced Layzner Wing Unit: Ground Only | Enh. Layzner Wing Unit: Ground | ERRO width 430>332; ": Ground" (see doubts)
- menu3000#72 | ブルグレン | Bull Gren | Bullgrenn | ERRO glossary: ブルグレン = Bullgrenn
- menu3000#75 | エステバリス 陸戦フレーム：地上専用 | Aestivalis Ground Frame: Ground Only | Aestivalis Ground Frame: Ground | ERRO width 384>332; ": Ground" (see doubts)
- menu3000#76 | エステバリス 空戦フレーム：地上専用 | Aestivalis Aerial Frame: Ground Only | Aestivalis Aerial Frame: Ground | ERRO width 372>332; ": Ground"
- menu3000#79 | エステバリス 砲戦フレームプロトタイプ | Aestivalis Artillery Frame Prototype | Aestivalis Artillery Frame Proto. | ERRO width 360>332
- menu3000#81 | ＶＦ－1Ａ スーパーバルキリー：宇宙専用 | VF-1A Super Valkyrie: Space Only | VF-1A Super Valkyrie: Space | ERRO width 338>332; ": Space" (see doubts)
- menu3000#83 | ＶＦ－1Ｓ ストライクバルキリー：宇宙専用 | VF-1S Strike Valkyrie: Space Only | VF-1S Strike Valkyrie: Space | ERRO width 336>332; ": Space"
- menu3000#92 | オウカオー | Oukaoh | Oukaou | ERRO glossary: オウカオー = Oukaou

### xm_menu3001_01 (4 fixes)

- menu3001#1 | スクロール：㊤㊦　戻る：×　終了：○ | Scroll: ㊤㊦ Back: × End: ○ | Scroll: ㊤㊦　Back: ×　Exit: ○ | ideographic spaces as in the JP; 終了 = Exit (approved hud3013#24)
- menu3001#21 | 撃墜ポイント詳細 | Shot Down Point Details | Kill Point Details | approved: 撃墜ポイント = Kill Points (hud3013#31; menu3001#11 auto)
- menu3001#22 | 撃墜数 | Shot Down Count | Kill Count | 撃墜数 = number of kills; consistent with Kill Points
- menu3001#39 | ここではプレイしたミッションの成果を確認できます。 | Here you can review your performance in the played mission. | Review the results of your mission. | ERRO width 610>378 (1 line)

### xm_menu3002_01 (1 fixes)

- menu3002#11 | サポートデバイス | Support Device | Support Dev. | ERRO width 148>146 (see doubts: menu3002#3 repeats menu3001#3 "Recovery Device", 160 px)

### xm_menu3004_01 (11 fixes)

- menu3004#0 | 選択：㊤㊦　決定：○ | Select: ㊤㊦ Confirm: ○ | Select: ㊤㊦　OK: ○ | ideographic space; 決定 = OK (approved common#7, hud3013#24)
- menu3004#1 | 選択：㊤㊦　戻る：×　決定：○ | Select: ㊤㊦ Back: × Confirm: ○ | Select: ㊤㊦　Back: ×　OK: ○ | ERRO width 303>283; ideographic spaces; OK
- menu3004#6 | クリアミッション | Clear Mission | Missions Cleared | status label (a count); "Clear Mission" read as a command
- menu3004#17 | ユニットや戦艦などを閲覧します | View units, battleships, and more | View units, battleships, etc. | ERRO width 327>283
- menu3004#18 | 人物／用語などの解説を確認します | Check descriptions of characters and terms | Look up people, terms, etc. | ERRO width 422>283; keeps など
- menu3004#19 | 送られてきたメールを確認します | Check received mail messages | Check received mail | ERRO width 290>283
- menu3004#20 | 世界情勢の動向を確認します | Check developments in world affairs | Check world situation trends | ERRO width 359>283; 世界情勢 = World Situation (approved menu3010#7), 動向 = trends
- menu3004#21 | 戦闘シミュレータで演習を行います | Run training exercises in combat simulator | Train in a combat simulator | ERRO width 426>283
- menu3004#27 | 大気圏内のフィールドで演習します | Train in an atmospheric field | Train in atmospheric field | ERRO width 291>283
- menu3004#28 | 宇宙空間のフィールドで演習します | Train in an outer space field | Train in outer space field | ERRO width 286>283 (pair with #27)
- menu3004#30 | ここではキャンペーン中の各種情報を\n参照することができます。\nまた、演習ミッションやオプション設定、\nゲームのセーブなども行えます。 | Here you can reference various information\nduring the campaign.\nYou can also run training missions, adjust options,\nor save game data. | Here you can view various\ncampaign information, run\ntraining missions, change\noptions, and save the game. | ERRO width 506>283 (4 lines); full meaning kept

### xm_menu3009_01 (6 fixes)

- menu3009#0 | 選択：㊤㊦　決定：○　インターミッションに戻る：× | Select: ㊤㊦ Confirm: ○ Return to Intermission: × | Select: ㊤㊦　OK: ○　Return to Intermission: × | ideographic spaces; OK
- menu3009#1 | 選択：㊤㊦　ジャンプ：⑤／①　タイトルリスト：□　決定：○　戻る：× | Select: ㊤㊦ Jump: ⑤/① Title List: □ Confirm: ○ Back: × | Select: ㊤㊦　Jump: ⑤/①　Title List: □　OK: ○　Back: × | ideographic spaces; OK
- menu3009#2 | 移動：⑮　旋回：⑰　拡大：⑤　縮小：①　リセット：⑩　次ユニット：⑦　前ユニット：③\nタイプ変更：□　コマンドリスト：○　戻る：× | Move: ⑮ Rotate: ⑰ Zoom In: ⑤ Zoom Out: ① Reset: ⑩ Next Unit: ⑦ Prev Unit: ③\nChange Type: □ Command List: ○ Back: × | Move: ⑮　Rotate: ⑰　Zoom+: ⑤　Zoom-: ①　Reset: ⑩　Next: ⑦\nPrev: ③　Change Type: □　Command List: ○　Back: × | ERRO width 789>571 (2 lines); Zoom+/Zoom- and Next/Prev to fit, glossary "Command List" and "Change Type" kept
- menu3009#3 | 移動：⑮　旋回：⑰　拡大：⑤　縮小：①　リセット：⑩　次ユニット：⑦　前ユニット：③\nコマンドリスト：○　戻る：× | Move: ⑮ Rotate: ⑰ Zoom In: ⑤ Zoom Out: ① Reset: ⑩ Next Unit: ⑦ Prev Unit: ③\nCommand List: ○ Back: × | Move: ⑮　Rotate: ⑰　Zoom+: ⑤　Zoom-: ①　Reset: ⑩　Next: ⑦\nPrev: ③　Command List: ○　Back: × | ideographic spaces; same layout as #2
- menu3009#4 | 移動：⑮　旋回：⑰　拡大：⑤　縮小：①　リセット：⑩　次ユニット：⑦　前ユニット：③\n戻る：× | Move: ⑮ Rotate: ⑰ Zoom In: ⑤ Zoom Out: ① Reset: ⑩ Next Unit: ⑦ Prev Unit: ③\nBack: × | Move: ⑮　Rotate: ⑰　Zoom+: ⑤　Zoom-: ①　Reset: ⑩　Next: ⑦\nPrev: ③　Back: × | ideographic spaces; same layout as #2
- menu3009#5 | 選択：㊤㊦　旋回：⑰　決定：○　戻る：× | Select: ㊤㊦ Rotate: ⑰ Confirm: ○ Back: × | Select: ㊤㊦　Rotate: ⑰　OK: ○　Back: × | ideographic spaces; OK

### xm_menu3013_01 (7 fixes)

- menu3013#0 | 選択：㊤㊦　決定：○　戻る：× | Select: ㊤㊦  Confirm: ○  Back: × | Select: ㊤㊦　OK: ○　Back: × | ERRO double ASCII space -> ideographic spaces as in the JP; OK
- menu3013#1 | 選択：㊤㊦　ジャンプ：①／⑤　戻る：× | Select: ㊤㊦  Jump: ①/⑤  Back: × | Select: ㊤㊦　Jump: ①/⑤　Back: × | ERRO double space
- menu3013#2 | 選択：㊤㊦ ジャンプ：①／⑤ パラメータ：△ タイトルリスト：□ 決定：○ 戻る：× | Select: ㊤㊦ Jump: ①/⑤ Params: △ Titles: □ Confirm: ○ Back: × | Select: ㊤㊦ Jump: ①/⑤ Stats: △ Titles: □ OK: ○ Back: × | ERRO width 620>568; this JP row uses single ASCII spaces, kept; パラメータ = Stats
- menu3013#3 | 選択：㊤㊦　パラメータ：△ タイプ変更：□　決定：○　戻る：× | Select: ㊤㊦  Params: △ Change Type: □  Confirm: ○  Back: × | Select: ㊤㊦　Stats: △ Change Type: □　OK: ○　Back: × | ERRO double space + width 599>568; the JP spacing mix (IS, ASCII, IS, IS) kept
- menu3013#4 | 選択：㊤㊦　ジャンプ：①／⑤　決定：○　戻る：× | Select: ㊤㊦  Jump: ①/⑤  Confirm: ○  Back: × | Select: ㊤㊦　Jump: ①/⑤　OK: ○　Back: × | ERRO double space
- menu3013#68 | 反動耐久 | Recoil Durability | Recoil Resistance | 反動耐久 = resistance to hit recoil/stagger, not "durability"
- menu3013#70 | 実弾防御 | Physical Defense | Ballistic Defense | 実弾 = solid/live ammunition (vs. beam in #69); "Physical" clashes with 物理攻撃 in #92

### xm_menu3013_02 (5 fixes)

- menu3013#93 | 出撃選択を中止して\nフリーミッションへ戻ります。\nよろしいですか？ | Cancel sortie select and return\nto Free Mission?\nAre you sure? | Cancel sortie selection and return\nto Free Mission.\nAre you sure? | JP is a statement + "Are you sure?"; EN asked two questions
- menu3013#96 | 出撃選択を中止して\nインターミッションへ戻ります。\nよろしいですか？ | Cancel sortie select and return\nto Intermission?\nAre you sure? | Cancel sortie selection and return\nto Intermission.\nAre you sure? | same as #93
- menu3013#106 | ここではプレイヤーユニットにモジュールを\n装備させることができます。\n１回の出撃につき、１つまで装備可能です。\nモジュールを装備すると特殊効果が発動し、\nミッションを優位に進めることができます。\n出撃するだけで消費するタイプと、\nミッション中に自動的に発動することで\n消費するタイプがあります。 | Equip a module on the player unit here.\nUp to 1 module can be equipped per sortie.\nModules provide special effects for an advantage.\nSome are consumed merely by sortying, while others\nare consumed when activated automatically in mission. | Here you can equip modules on the player unit.\nUp to one module can be equipped per sortie.\nAn equipped module triggers a special effect\nthat gives you an edge in the mission.\nSome are used up just by sortieing, while\nothers are used up when they trigger\nautomatically during a mission. | restores the dropped clause (特殊効果が発動し、ミッションを優位に進める) and fixes "sortying"
- menu3013#108 | ユニットを応急修理しますが、よろしいですか？\n\n%d － %d ＝ %d | Perform emergency repair on unit?\n\n%d - %d ＝ %d | Perform emergency repair on the unit?\n\n%d - %d -> %d | ERRO forbidden ＝ (ASCII = is forbidden too) -> "->"
- menu3013#119 | %s を編入させます。\nよろしいですか？\n\n%d － %d ＝ %d | Admit %s?\nAre you sure?\n\n%d - %d ＝ %d | Admit %s?\nAre you sure?\n\n%d - %d -> %d | ERRO forbidden ＝ -> "->"

### xm_menu3013_03 (3 fixes)

- menu3013#182 | 通常移動、ダッシュ時の旋回性を強化します | Enhances turning ability during normal movement and dash | Enhances turning in normal movement and dashes | ERRO width 599>568
- menu3013#184 | コンボの追加、換装追加、進化などを行います | Performs combo additions, equipment additions, evolution, etc. | Adds combos and equipment, evolves units, etc. | ERRO width 617>568
- menu3013#194 | ユニットを進化させると、キャンペーン中は\n進化前のユニットを使用できなくなります。\n（フリーミッション、対戦では使用可能）\n\nこのユニットを進化させますか？ | Evolving a unit prevents using its pre-evolution\nform during the campaign (usable in Free\nMission and VS Battle).\n\nEvolve this unit? | Evolving a unit prevents using its pre-evolution\nform during the campaign (usable in Free\nMission and Versus).\n\nEvolve this unit? | 対戦 = Versus (approved hud3013 "Versus Menu")

### xm_menu3018_01 (13 fixes)

- menu3018#0 | ジオン公国残党軍 | Principality of Zeon Remnants | Zeon Remnant Forces | ERRO width 301>231 (see doubts: 公国 dropped)
- menu3018#2 | 統一帝国ギガノス | United Empire of Giganos | Giganos Empire | ERRO width 254>231; glossary 統一帝国ギガノス = Unified Empire of Giganos does not fit (234 px even as "Unified Giganos Empire"); glossary short form ギガノス帝国 = Giganos Empire (see doubts)
- menu3018#5 | 木連 | Jovian Union | Jovian Federation | glossary: 木連 = Jovian Federation ("Jovian Union" passed only on the word "Jovian")
- menu3018#6 | ドレイク軍 | Drake Forces | Drake Army | consistency with glossary ポセイダル軍 = Poseidal Army
- menu3018#8 | グラドス帝国 | Gradosian Empire | Grados Empire | glossary: Grados Empire
- menu3018#15 | 地球連邦政府 | Earth Federation Government | Earth Federation Gov't | ERRO width 290>231
- menu3018#16 | 連合宇宙軍 | Allied Space Forces | U.E. Space Force | glossary 連合宇宙軍 = United Earth Space Force (250 px, does not fit 231): abbreviated (see doubts)
- menu3018#21 | 機動戦艦ナデシコ | Mobile Battleship Nadesico | Battleship Nadesico | ERRO width 261>231 (see doubts)
- menu3018#26 | ネルガル重工 | Nergal Heavy Industries | Nergal Heavy Ind. | ERRO width 238>231
- menu3018#37 | アルバトロ・ミル・ジュリア・アスカ | Albatro Mill Julia Asuka | Albatro Mill J. Asuka | ERRO width 243>231
- menu3018#57 | ゲキ・ガンガー３ | Geki-Gangar 3 | Gekiganger 3 | glossary (provisional decision): ゲキ・ガンガー = Gekiganger
- menu3018#65 | ギガノス機動要塞 | Giganos Mobile Fortress | Giganos Mob. Fortress | ERRO width 234>231
- menu3018#67 | コンペイトウ | Confeito | Konpei Island | ERRO glossary: コンペイトウ = Konpei Island (also approved menu3010#30)

## Recurring labels settled (JP -> EN), for harmonising the other screens

| JP | EN | Source / note |
|---|---|---|
| 選択：㊤㊦ | Select: ㊤㊦ | approved hud3013#24 |
| 決定：○ | OK: ○ | approved common#7, hud3013#24 (not "Confirm") |
| 戻る：× | Back: × | approved hud3013#25 |
| 終了：○ / 終了：⑪ | Exit: ○ / Exit: ⑪ | approved hud3013#24, menu3010#0 |
| スキップ：○ | Skip: ○ | |
| スクロール：㊤㊦ | Scroll: ㊤㊦ | |
| ジャンプ：①／⑤ | Jump: ①/⑤ | (hud3013 has ページジャンプ = Page:) |
| タイトルリスト：□ | Title List: □ (Titles: □ only where width forces, menu3013#2) | |
| パラメータ：△ | Stats: △ | |
| タイプ変更：□ | Change Type: □ | |
| コマンドリスト：○ | Command List: ○ | glossary |
| 旋回：⑰ (viewer) | Rotate: ⑰ | 旋回性能 (unit stat) = Turning |
| 拡大：⑤ / 縮小：① | Zoom In / Zoom Out (Zoom+ / Zoom- in menu3009#2-4 for width) | |
| 次ユニット / 前ユニット | Next Unit / Prev Unit (Next / Prev in menu3009#2-4) | |
| インターミッションに戻る | Return to Intermission | approved hud3013#11 |
| インターミッション | Intermission | glossary |
| フリーミッション | Free Mission | glossary |
| 対戦 | Versus | approved hud3013 (Versus Menu) |
| 出撃 | Sortie | |
| 出撃選択 | Sortie Select | |
| 閲覧 | Viewer | |
| 事典 | Encyclopedia | |
| 通信ログ | Comm Log | |
| 演習 | Training | |
| オプション | Options | |
| セーブしますか？ | Save game? | |
| エースポイント | Ace Points | glossary |
| モジュール | Module | glossary |
| ユニット経験値 | Unit EXP | |
| 撃墜ポイント | Kill Points | approved hud3013#31 |
| 撃墜数 | Kill Count | |
| 僚機 | Wingman | approved hud3013#39 |
| プレイヤーユニット | Player Unit(s) | see doubt 3 |
| アーマー | Armor (HP gauge) | |
| ユニット強化 | Unit Upgrade | |
| 特殊強化 | Special Upgrade | |
| ユニット編入 | Unit Admission (game's own header ＡＤＭＩＳＳＩＯＮ) | |
| 応急修理 | Emergency Repair | |
| 進化 | Evolution | |
| 連携 / 連携度 | Cooperation / Cooperation Level | |
| 実弾 | ballistic (実弾防御 = Ballistic Defense; module バレットアーマー = Bullet Armor) | |
| ㍉確認 | ㍉Confirm | approved hud3013#41 |
| ㌢警告 | ㌢Warning | |
| ：地上専用 / ：宇宙専用 (unit lists) | : Ground Only / : Space Only (": Ground" / ": Space" where 332 px forces it) | see doubt 1 |
| ％ after a number | ％ (full-width, kept) | PLANO |
| ＝ in formulas | -> | ＝ and = are both forbidden |

## Doubts not changed / for the owner

1. **menu3000 terrain suffix**: ": Ground Only"/": Space Only" kept where it fits; #71, #75, #76, #81, #83 had to use
   ": Ground"/": Space" to fit the provisional 332 px. When the box is measured, either restore "Only" there or adopt
   the short form on all 18 rows for uniformity. #67 "Layzner Mk-II Concept (Flight)" drops "Ver." and "Mode" (#66 says
   "Concept Ver.", #65 "(Flight Mode)"); #79 "Artillery Frame Proto."; #69-71 "Enh." (#68 stays "Enhanced Layzner").
2. **Repeat rows that inherit a wider string**: menu3002#3 repeats menu3001#3 "Recovery Device" (160 px > 146 px in
   menu3002). Add an auto override menu3002#3 = "Recovery Dev." (matches my menu3002#11 "Support Dev."), or measure the
   module box. Same for the other tiers if the box is really 146 px.
3. menu3013#5 repeats menu3009#7 "Player Units" (viewer category, plural); in the sortie screen it is the single player
   slot next to "Wingman Unit 1/2". Suggest an override menu3013#5 = "Player Unit".
4. **Names not in the glossary** (please add): ウィングキャリバー = Wing Caliber (changed from "Wing Calibur"; SRW/Dunbine
   usage, verify), キャバリアー = Cavalier (kept), ブローラー = Prowler (kept; L-Gaim Mk-II's flight form, verify Prowler vs
   Brawler), ステイメン = Stamen, ランドブースター = Land Booster, アモンデュール・スタック = Amon Duule Stack,
   ガンダム試作１号機Ｆｂ = Gundam GP01-Fb (official RX-78GP01Fb, no hyphen), エステバリス（アキト専用） = Aestivalis (Akito
   Custom) (glossary has アキト専用機 = "Aestivalis (Akito C.)", different JP, kept), ウィングガンダムゼロカスタム = Wing Gundam
   Zero Custom (glossary has ウイングガンダムゼロ(EW版) = "Wing Gundam Zero (EW)"; decide if they are the same).
5. **menu3018 (231 px) compromises**: #0 "Zeon Remnant Forces" (公国 "Principality" dropped; "Principality of Zeon
   Remnants" = 301 px); #2 "Giganos Empire" (glossary formal "Unified Empire of Giganos" cannot fit; uses the glossary
   short form); #16 "U.E. Space Force" (glossary "United Earth Space Force" = 250 px); #21 "Battleship Nadesico" (機動
   dropped); #26 "Nergal Heavy Ind."; #37 "Albatro Mill J. Asuka"; #65 "Giganos Mob. Fortress". All wait for the box
   measurement; the full forms should come back if the index box is wider than the widest JP line.
6. menu3013#67 装甲 "Armor" is identical to #32 アーマー "Armor" (HP) on the same screen. Not changed (unknown which
   stat it is); consider "Armor Rating" or "Plating" after seeing the screen.
7. menu3004#5 ユニット "Unit": probably a count ("Units") next to Ace Points / Missions Cleared; not changed without the
   screen.
8. menu3013#135 強化終了 "Upgrade Complete" may be "Max Level" (shown after レベル９); #160 出撃不可エリア "Unavailable
   Area" may be clearer as "Cannot Sortie Here"; #47 (auto, from hud3013) ends with a period while the other one-line
   help strings of menu3013 have none. Not changed.
9. menu3013#108/#119: "%d - %d -> %d" replaces ＝ (no = glyph allowed). If the menu font has ＝, the owner may prefer to
   allow it.
10. xc m6322#21 早く…消えなさい！ "Hurry and... disappear!": addressee ambiguous (enemy vs. Tak); EN keeps the ambiguity,
    not changed. m6325#4 この星 rendered "Earth" (kept; "this planet" would be closer and colder but does not fit with the
    rest of the line). m6320#1 "2-unit combat training" (２機１組 = pairs) kept as acceptable.
11. Dates: "July 054", "October 054", "March 055", "April 056", "November 056", "April 057": consistent, kept.
