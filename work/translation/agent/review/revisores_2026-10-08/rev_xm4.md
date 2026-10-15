# Review rev_xm4: menu3061-3063, 3065, 3068-3073, 3076, 3077

Proposals: `rev_xm4.json` (121 lines; `check_fixes.py` prints "0 proposed lines with errors").
Every **ERRO** row of the 12 validation reports is covered except **menu3077#54** (it cannot pass; see "Blocked" below).

## What each screen is

- **menu3061**: name list of enemy/"Another" units (Gundam, Dunbine, L-Gaim, Dragonar, Nadesico, Brain Powerd, Layzner, ACE originals); used by the Viewer. Box 235 px.
- **menu3062**: name list of minor enemies, weapons/objects and ships (missiles, sub-cannons, turrets, Batta...). Box 136 px.
- **menu3063**: name list of ships/carriers (Dunbine, L-Gaim, Dragonar, Nadesico, Gundam, Macross). Box 189 px.
- **menu3065**: new-game setup wizard (Favorite Title, Difficulty, Controller type, Flight controller, Auto Altitude, Ace bonus from ACE1 save, Vibration, Quick Turn, final summary). Box 437 px.
- **menu3068**: Options top menu (Game / Controller / Sound / Screen) with one-line help texts and the reset dialog. Box 240 px.
- **menu3069**: "Update Information" pop-up after an operation (unit joined/left, evolution/admission/Special Upgrade available, new menu entries, new weapons). Box 314 px.
- **menu3070**: Options > Game (Difficulty, Lock Info, Target priority, Attack Demo, Text) with help lines. Box 313 px.
- **menu3071**: Options > Controller (Controller Type, Flight Type, Camera, Vibration, Quick Turn, Auto Altitude, Key Assign) with help lines. Box 350 px.
- **menu3072**: Options > Sound (volumes, attack voice, BGM test/type, Stereo/Dolby, series titles for the BGM test). Box 400 px.
- **menu3073**: Options > Screen (Brightness, Contrast). Box 227 px.
- **menu3076**: Key Assign screen (1P/2P controller, functions, help lines, duplicate-button warning). Box 332 px.
- **menu3077**: name list of player units (VS/Viewer). Box 185 px.

## Fixes

ref | JP | old EN | new EN | reason
---|---|---|---|---
menu3061#1 | ゲルググＭ（シーマ） | Gelgoog M (Cima) | Gelgoog Marine (Cima) | GLOSSARIO: Gelgoog Marine (Cima); matches #0 "Gelgoog Marine" and unit_names
menu3061#34 | カルバリー・テンプル（クワサン） | Calvary Temple (Quwasan) | Calvary T. (Quwasan) | too wide for provisional box (ERRO); "Calvary T." abbreviation keeps both names
menu3061#38 | ダイン・マッフ | Dyne Maff | Deins MAFFU | ERRO glossary: ダイン = Deins; マッフ = MAFFU as in GLOSSARIO ファルゲン・マッフ = Falguen MAFFU (menu3000#46, menu3061#51)
menu3061#41 | ゲバイ・マッフ | Gwei Maff | Gwei MAFFU | マッフ = MAFFU (GLOSSARIO, same list as Falguen MAFFU)
menu3061#47 | スターク・ガンドーラ（ガンツァー） | Stark Ghandora (Guntzer) | S. Gan Dolla (Guntzer) | GLOSSARIO: Stark Gan Dolla (was "Ghandora"); too wide for provisional box (ERRO), "S." abbreviation
menu3061#48 | スターク・ガンドーラ（ドーラ） | Stark Ghandora (Dora) | Stark Gan Dolla (Dolla) | GLOSSARIO: Stark Gan Dolla; ドーラ is the "Dolla" half of ガンドーラ
menu3061#49 | ゲバイ・マッフ（ＳＰ） | Gwei Maff (SP) | Gwei MAFFU (SP) | マッフ = MAFFU (GLOSSARIO)
menu3061#52 | ギルガザムネ（グンジェム） | Gilgazamune (Gun Jem) | Gilgazamune (Gon Jem) | GLOSSARIO: グン・ジェム = Gon Jem (hud3021/menu3014 approved); "Gun Jem" was wrong
menu3061#54 | ギルガザムネ（ドルチェノフ） | Gilgazamune (Dorchenov) | Gilgazamune Dorchenov | too wide for provisional box (ERRO); both glossary names required, parentheses do not fit (235 px exactly)
menu3061#56 | ゲルフ・マッフ | Gelf Maff | Gelf MAFFU | マッフ = MAFFU (GLOSSARIO)
menu3061#58 | ヤクトゲルフ・マッフ | Jagd Gelf Maff | Jagd Gelf MAFFU | マッフ = MAFFU (GLOSSARIO)
menu3061#60 | レビゲルフ・マッフ | Rebi Gelf Maff | Reb Gelf MAFFU | GLOSSARIO: レビゲルフ = Reb Gelf (unit_names #81); マッフ = MAFFU
menu3061#67 | ヤテンコウ | Yatenkou | Yatenko | GLOSSARIO: 夜天光 = Yatenko (research note: the game also writes it ヤテンコウ in one menu)
menu3061#70 | 巨大バロンズゥ | Giant Baronzwo | Giant Baronz | GLOSSARIO: バロンズゥ = Baronz (entry notes 巨大バロンズゥ); "Baronzwo" invented
menu3061#80 | エルダール | Eldarl | El Darr | ERRO glossary: El Darr
menu3061#81 | ダンコフ | Dankov | Dankova | ERRO glossary: Dankova
menu3061#86 | ブラッディカイザル | Bloody Kaisar | Bloodykaisar | research lgaim_layzner.json: ブラッディカイザル = Bloodykaisar, like Grimekaisar (unit_names #21)
menu3061#101 | ガンアーク（マリナ機） | Gun Ark (Marina Custom) | Gun Ark (Marina) | too wide for provisional box (ERRO); same pattern as menu3000#88 "Gun Ark (Tak)"
menu3061#104 | クァドラン・ロー（量産） | Queadluun-Rau (Mass Production) | Queadluun-Rau (Mass) | too wide for provisional box (ERRO); 量産 = mass-production version (vs #105 "(Milia)")
menu3062#3 | トランスユニット | Trance Unit | Trans Unit | GLOSSARIO/tutorial m6302: Trans Unit ("Trance" misspelt)
menu3062#6 | チャフグレネード | Chaff Grenade | Chaff Gren. | too wide for provisional box (ERRO) (136 px box)
menu3062#10 | ダミーリーダー | Dummy Leader | Decoy Leader | too wide for provisional box (ERRO); ダミー = decoy, same meaning
menu3062#11 | クレープス | Kreb | Krebs | クレープス = German Krebs (Cancer), same German-zodiac naming as Loewe/Waage/Stier; "Kreb" is not a word
menu3062#12 | サブキャノン０１ | Sub Cannon 01 | Sub Cann. 01 | too wide for provisional box (ERRO)
menu3062#13 | サブキャノン０２ | Sub Cannon 02 | Sub Cann. 02 | too wide for provisional box (ERRO)
menu3062#14 | サブキャノン０４ | Sub Cannon 04 | Sub Cann. 04 | too wide for provisional box (ERRO)
menu3062#15 | サブキャノン０３ | Sub Cannon 03 | Sub Cann. 03 | too wide for provisional box (ERRO)
menu3062#16 | サブキャノン０５ | Sub Cannon 05 | Sub Cann. 05 | too wide for provisional box (ERRO)
menu3062#26 | 多砲塔戦車 | Multi-Turret Tank | Multi-Turret | too wide for provisional box (ERRO); no form with "Tank" fits 136 px (see doubts)
menu3062#29 | 重攻撃機 | Heavy Attacker | Hvy Attacker | too wide for provisional box (ERRO); m6211 uses "heavy attacker"
menu3062#34 | キライ | Space Mine | Mine | 機雷 = mine; "Space" was added
menu3062#36 | ウィル・ウィプス | Will Wips | Will Wipps | GLOSSARIO: Will Wipps
menu3063#10 | サージェ・オーパス | Serge Opus | Sarge Opus | GLOSSARIO: Sarge Opus
menu3063#17 | 大型輸送哨戒機 | Large Transport Patrol Aircraft | Lg. Patrol Airlifter | too wide for provisional box (ERRO); large + patrol + transport aircraft kept
menu3063#19 | 宇宙高速艇 | Space High-Speed Craft | Space Speedboat | too wide for provisional box (ERRO); 高速艇 = speedboat
menu3063#20 | チューリップ | Tulip | Chulip | GLOSSARIO: Chulip (used in all briefings/missions)
menu3063#36 | ピケット艦（ゼントラン） | Picket Ship (Zentran) | Picket (Zentran) | too wide for provisional box (ERRO); picket = picket ship
menu3063#37 | ミリア艦（メルトラン） | Milia Ship (Meltran) | Meltran Milia Ship | too wide for provisional box (ERRO)
menu3063#39 | ピケット艦（メルトラン）  | Picket Ship (Meltran) | Picket (Meltran) | too wide for provisional box (ERRO)
menu3063#40 | 標準戦艦（ゼントラン） | Standard Battleship (Zentran) | Std. Ship (Zentran) | too wide for provisional box (ERRO); 標準戦艦 = standard warship
menu3063#41 | 標準戦艦（メルトラン） | Standard Battleship (Meltran) | Std. Ship (Meltran) | too wide for provisional box (ERRO)
menu3063#43 | ブリタイ艦 | Britai Ship | Vrlitwhai's Ship | GLOSSARIO: ブリタイ艦 = Vrlitwhai's Ship (also menu3034/briefings)
menu3065#0 | 選択：㊤㊦ 決定：○　戻る：× | Select: ㊤㊦  Confirm: ○  Back: × | Select: ㊤㊦ OK: ○　Back: × | ERRO double space; 決定 = "OK" as approved common#7/hud3013#24; JP separator kept (ASCII space, then 　)
menu3065#1 | 選択：㊤㊦ 決定：○　メニューに戻る：× | Select: ㊤㊦  Confirm: ○  Return to Menu: × | Select: ㊤㊦ OK: ○　Return to Menu: × | same as #0
menu3065#2 | ㍉初期設定確認 | ㍉Initial Setup Confirmation | ㍉Initial Settings Confirmation | row reused by menu3068#11/menu3071#39 (reset-to-defaults dialogs): "Initial Settings" fits both contexts, "Setup" only the new-game one
menu3065#7 | 「お気に入りタイトル」を選択すると、そのタイトルに属する / ユニットに対して、ユニット経験値の獲得量の増加、 | Selecting a Favorite Title grants advantages to units / belonging to that title, such as increased unit EXP, | Choosing a "Favorite Title" gives its units / benefits such as more unit EXP gained, | too wide for provisional box (ERRO); 「」 -> quotes
menu3065#8 | 連携力が向上するなどのメリットが発生します。 / お気に入りタイトルはキャンペーン中に変更はできません。 | improved cooperation ability, and other benefits. / Favorite Title cannot be changed during campaign. | improved teamwork, and other benefits. / The title can't be changed in a campaign. | too wide for provisional box (ERRO); full meaning kept
menu3065#14 | 難易度はゲーム中にいつでも変更が可能です。 | Difficulty can be changed at any time during the game. | Difficulty can be changed anytime in-game. | too wide for provisional box (ERRO)
menu3065#35 | 使用ウェポンを切り替えるタイプの操作方法です。 / Ｌ１ボタンでウェポンを選択し、□ボタンで決定、使用します。 | A control method where you switch weapons in use. / Select weapon with L1 button, confirm and fire with □ button. | A type that switches the weapon in use. / Select with L1, confirm and fire with □. | too wide for provisional box (ERRO)
menu3065#36 | ウェポンは方向キー上下を使って選択することもできます。 / コントローラタイプはゲーム中に切替が可能です。 | Weapons can also be selected using directional buttons Up/Down. / Controller type can be changed during gameplay. | D-pad Up/Down can also select weapons. / Controller type can be changed in-game. | too wide for provisional box (ERRO)
menu3065#37 | 使用ウェポンを瞬時に選択できる操作方法です。 / Ｌ１ボタンを押しながら、○、△、□、×、Ｒ１、Ｒ２ボタンを押すと | A control method allowing instant weapon selection. / Hold L1 button and press ○, △, □, ×, R1, or R2 button | A control type for instant weapon selection. / Hold L1 and press ○, △, □, ×, R1, or R2 | too wide for provisional box (ERRO)
menu3065#38 | 設定されているウェポンで攻撃ができます。 / コントローラタイプはゲーム中に切替が可能です。 | to attack with the assigned weapon. / Controller type can be changed during gameplay. | to attack with the assigned weapon. / Controller type can be changed in-game. | too wide for provisional box (ERRO)
menu3065#42 | 「Ａｎｏｔｈｅｒ Ｃｅｎｔｕｒｙ’ｓ Ｅｐｉｓｏｄｅ」のゲームデータが / 見つかりました。 ゲーム開始時に所持エースポイントを / 20000ポイント増加させることができます。 / ゲーム開始時からユニットの改造などが行え、 / 優位にキャンペーンを進めることができます。 / エースポイントを増加しますか？ | Another Century's Episode game data was found. / You can increase starting Ace Points by 20000 points. / This lets you upgrade units from the start of the game, / granting an advantage in the campaign. / Increase Ace Points? | "Another Century's Episode" data was found. / You can start the game with 20000 extra / Ace Points, letting you upgrade units and / more from the start for a campaign edge. / Increase your Ace Points? | auto-wrap warning only; rewrapped by hand, title in quotes as 「」 requires, same content
menu3065#46 | お気に入りタイトル：　 | Favorite Title:  | Favorite Title:　 | ERRO trailing space: ":" + ideographic space as the JP "：　"
menu3065#47 | 難易度：　 | Difficulty:  | Difficulty:　 | same
menu3065#48 | コントローラ：　 | Controller:  | Controller:　 | same
menu3065#49 | フライトコントローラ：　 | Flight Controller:  | Flight Controller:　 | same
menu3065#50 | 自動高度調整：　 | Auto Altitude Adjustment:  | Auto Altitude Adjustment:　 | same
menu3065#51 | ボーナスポイント：　 | Bonus Points:  | Bonus Points:　 | same
menu3065#52 | バイブレーション：　 | Vibration:  | Vibration:　 | same
menu3065#65 | 簡単に操作できる初心者向けの操作方法です。 / 左スティックを左右に倒すとユニットが旋回し、 | A simple control method suitable for beginners. / Tilting left stick left/right turns the unit, | An easy control type for beginners. / Left stick left/right turns the unit, | too wide for provisional box (ERRO)
menu3065#66 | 左スティックを放すと自動的に水平に戻ります。 | and releasing the left stick automatically levels the craft. | and releasing the stick auto-levels the unit. | too wide for provisional box (ERRO)
menu3065#67 | 回転と上昇下降を使用する上級者向けの操作方法です。 / 左スティックを左右に倒すと回転（ロール）し、 | An advanced control method using rotation, ascent, and descent. / Tilting left stick left/right rolls the unit, | An expert type using roll and climb/dive. / Left stick left/right rolls the unit, | too wide for provisional box (ERRO)
menu3065#68 | 前後に倒すと上昇／下降（ピッチ）を行います。 / 左スティックを放してもユニットの向きは変わりません。 | and tilting forward/back pitches up/down. / Releasing the left stick does not change heading. | and forward/back pitches up/down. / Releasing the stick keeps its orientation. | too wide for provisional box (ERRO); 向きは変わりません = orientation stays (does not auto-level), "heading" was off
menu3065#69 | 左スティックの前後が下降／上昇になるリバース操作です。 / 左スティックを左右に倒すとユニットが旋回し、 | Reverse controls where left stick forward/back pitches down/up. / Tilting left stick left/right turns the unit, | Reversed: stick forward/back is down/up. / Left stick left/right turns the unit, | too wide for provisional box (ERRO); forward/back order kept (normal = up/down, reverse = down/up)
menu3065#70 | 左スティックを放すと自動で水平に戻ります。 | and releasing the left stick automatically levels the craft. | and releasing the stick auto-levels the unit. | too wide for provisional box (ERRO)
menu3065#71 | 左スティックの前後が下降／上昇になるリバース操作です。 / 左スティックを左右に倒すと回転（ロール）し、 | Reverse controls where left stick forward/back pitches down/up. / Tilting left stick left/right rolls the unit, | Reversed: stick forward/back is down/up. / Left stick left/right rolls the unit, | too wide for provisional box (ERRO)
menu3065#72 | 前後に倒すと下降／上昇（ピッチ）を行います。 / 左スティックを放してもユニットの向きは変わりません。 | and tilting forward/back pitches down/up. / Releasing the left stick does not change heading. | and forward/back pitches down/up. / Releasing the stick keeps its orientation. | too wide for provisional box (ERRO)
menu3065#75 | クイックターン：　 | Quick Turn:  | Quick Turn:　 | same
menu3065#78 | キャンペーンを新しく開始してよろしいでしょうか？ | Start a new campaign with these settings? | Start a new campaign. Are you sure? | "with these settings" was added; JP only asks to confirm starting a new campaign
menu3068#7 | ゲームのプレイ環境を変更します | Change gameplay settings | Change game settings | too wide for provisional box (ERRO)
menu3068#8 | コントローラの設定を変更します | Change controller settings | Change controller setup | too wide for provisional box (ERRO)
menu3068#10 | テレビ画面の設定を変更します | Change TV screen settings | Change TV screen setup | too wide for provisional box (ERRO)
menu3068#12 | 変更された内容を初期状態に / 戻します。 / よろしいですか？ | Reset changes to default settings? / Are you sure? | Reset all changes / to the default settings. / Are you sure? | auto-wrap warning only; JP is a statement + question, hand-wrapped to 3 lines
menu3069#6 | %s　の特殊強化が可能 | %s Special Upgrade available | %s Sp. Upgrade available | too wide for provisional box (ERRO)
menu3069#9 | 通信ログに受信メールが追加 | Received mail added to Comm Log | New mail added to Comm Log | too wide for provisional box (ERRO)
menu3069#12 | フリーミッションにＥＸミッションが追加 | EX Missions added to Free Mission | Free Mission: EX Mission added | too wide for provisional box (ERRO); "Free Mission: X added" pattern for #12-#13
menu3069#13 | フリーミッションにＣＯＭ対戦が追加 | COM Battle added to Free Mission | Free Mission: COM Battle added | too wide for provisional box (ERRO)
menu3069#15 | ＧＰ０１　に　ロングバレルライフル　が追加 | Long Barrel Rifle added to GP01 | GP01: Long Barrel Rifle added | too wide for provisional box (ERRO); "<unit>: <weapon> added" pattern for #15-#18
menu3069#16 | ガンアーク　に　ライフル（チャージ）　が追加 | Rifle (Charge) added to Gun Ark | Gun Ark: Rifle (Charge) added | too wide for provisional box (ERRO)
menu3069#17 | ガンアーク　に　ライフル（バースト）　が追加 | Rifle (Burst) added to Gun Ark | Gun Ark: Rifle (Burst) added | consistency with #16
menu3069#18 | ガンアーク　に　ガーディアン　が追加 | Guardian added to Gun Ark | Gun Ark: Guardian added | consistency with #16
menu3070#0 | 選択：㊤㊦　設定：㊧㊨　戻る：× | Select: ㊤㊦  Set: ㊧㊨  Back: × | Select: ㊤㊦　Set: ㊧㊨　Back: × | ERRO double space; ideographic space where the JP has it
menu3070#18 | 難易度をルーキー（やさしい）に変更します | Change difficulty to Rookie (Easy) | Set difficulty to Rookie (Easy) | too wide for provisional box (ERRO)
menu3070#19 | 難易度をパイロット（普通）に変更します | Change difficulty to Pilot (Normal) | Set difficulty to Pilot (Normal) | too wide for provisional box (ERRO)
menu3070#20 | 難易度をエース（難しい）に変更します | Change difficulty to Ace (Hard) | Set difficulty to Ace (Hard) | too wide for provisional box (ERRO)
menu3070#21 | ロックサイトの追加情報を表示します | Display additional lock sight information | Show extra lock sight info | too wide for provisional box (ERRO)
menu3070#22 | ロックサイトの追加情報を非表示にします | Hide additional lock sight information | Hide extra lock sight info | too wide for provisional box (ERRO)
menu3070#23 | カメラ内にいる敵を優先します | Prioritize enemies within camera view | Prioritize enemies on camera | too wide for provisional box (ERRO)
menu3070#24 | ユニットが向いている方向の敵を優先します | Prioritize enemies in facing direction | Prioritize enemies you face | too wide for provisional box (ERRO)
menu3070#26 | ダメージを多く受けている敵を優先します | Prioritize enemies that have taken more damage | Prioritize heavily damaged foes | too wide for provisional box (ERRO)
menu3070#27 | 攻撃時に発生するデモを再生します | Play in-game attack cinematics | Play attack cinematics | parallel with #28 ("in-game" dropped in both; JP 攻撃時に発生するデモ)
menu3070#28 | 攻撃時に発生するデモを再生しません | Do not play in-game attack cinematics | Do not play attack cinematics | too wide for provisional box (ERRO)
menu3070#29 | 通信メッセージを表示します | Display communication messages | Show comm messages | too wide for provisional box (ERRO); "comm" as in Comm Log
menu3070#30 | 通信メッセージを非表示にします | Hide communication messages | Hide comm messages | parallel with #29
menu3071#24 | 飛行操作を簡易操作にします | Set flight controls to Simple | Flight controls: Simple | parallel with #26/#27
menu3071#25 | 飛行操作をピッチ／ロールにします | Set flight controls to Pitch/Roll | Flight controls: Pitch/Roll | parallel with #26/#27
menu3071#26 | 飛行操作を簡易操作（リバース）にします | Set flight controls to Simple (Inverted) | Flight controls: Simple (Rev.) | too wide for provisional box (ERRO); リバース = Reverse, as the option labels "Easy Reverse"/"Flight Reverse"
menu3071#27 | 飛行操作をピッチ／ロール（リバース）にします | Set flight controls to Pitch/Roll (Inverted) | Flight controls: Pitch/Roll (Rev.) | too wide for provisional box (ERRO)
menu3071#30 | 上下左右をリバースにしてカメラを移動します | Move camera with both axes inverted | Move camera with X/Y inverted | too wide for provisional box (ERRO); parallel with #29 "Move camera with Y-axis inverted"
menu3071#33 | ユニットの向きを自動で対象の方向へ合わせます | Automatically orient unit toward target | Auto-turn unit toward the target | too wide for provisional box (ERRO)
menu3071#35 | 移動中、自動で対象との高度を合わせます | Automatically match altitude to target during movement | Auto-match target height in motion | too wide for provisional box (ERRO)
menu3071#36 | 任意で対象との高度を合わせます | Adjust altitude to target manually | Manually match target height | parallel with #35; 任意で = at will/manually
menu3071#37 | コントローラのボタン設定を変更します | Change controller button configuration | Change button assignments | too wide for provisional box (ERRO)
menu3072#1 | 選択：㊤㊦　設定：㊧㊨　再生：○　停止：× | Select: ㊤㊦  Set: ㊧㊨  Play: ○  Stop: × | Select: ㊤㊦　Set: ㊧㊨　Play: ○　Stop: × | ERRO double space; ideographic spaces as in the JP
menu3072#26 | ゲーム中、ボーカル付きのユニットＢＧＭを再生します | Play vocal unit BGM during gameplay | Play vocal unit BGM in-game | parallel with #27
menu3072#27 | ゲーム中、ボーカルなしのユニットＢＧＭを再生します | Play instrumental unit BGM during gameplay | Play instrumental unit BGM in-game | too wide for provisional box (ERRO)
menu3072#28 | ボーカル付き、ボーカルなしをランダムで再生します | Play vocal and instrumental BGM randomly | Play vocal/instrumental BGM at random | too wide for provisional box (ERRO)
menu3072#71 | 機動戦艦ナデシコ  Ｔｈｅ ｐｒｉｎｃｅ ｏｆ ｄａｒｋｎｅｓｓ | Martian Successor Nadesico: The Prince of Darkness | Nadesico: The Prince of Darkness | too wide for provisional box (ERRO); same as menu3022#6 second line
menu3073#6 | 画面の明るさを調整します | Adjust screen brightness | Set screen brightness | too wide for provisional box (ERRO)
menu3073#7 | 画面のコントラストを調整します | Adjust screen contrast | Set screen contrast | parallel with #6
menu3076#29 | 上昇（連続２回入力で上昇回避） | Ascend (tap twice for Ascend Evasion) | Ascend (tap twice: evade up) | too wide for provisional box (ERRO)
menu3076#30 | 下降（連続２回入力で下降回避） | Descend (tap twice for Descend Evasion) | Descend (tap twice: evade down) | too wide for provisional box (ERRO)
menu3076#41 | ウェポン２の使用（シフトメニュー起動時） | Use Weapon 2 (with Shift Menu open) | Use Weapon 2 (Shift Menu open) | too wide for provisional box (ERRO); 起動時 = while the Shift Menu is open
menu3076#42 | ウェポン３の使用（シフトメニュー起動時） | Use Weapon 3 (with Shift Menu open) | Use Weapon 3 (Shift Menu open) | too wide for provisional box (ERRO)
menu3076#43 | ウェポン４の使用（シフトメニュー起動時） | Use Weapon 4 (with Shift Menu open) | Use Weapon 4 (Shift Menu open) | too wide for provisional box (ERRO)
menu3076#44 | ウェポン５の使用（シフトメニュー起動時） | Use Weapon 5 (with Shift Menu open) | Use Weapon 5 (Shift Menu open) | too wide for provisional box (ERRO)
menu3076#45 | ウェポン６の使用（シフトメニュー起動時） | Use Weapon 6 (with Shift Menu open) | Use Weapon 6 (Shift Menu open) | too wide for provisional box (ERRO)
menu3076#46 | ウェポン７の使用（シフトメニュー起動時） | Use Weapon 7 (with Shift Menu open) | Use Weapon 7 (Shift Menu open) | too wide for provisional box (ERRO)
menu3076#56 | 複数の場所に同じボタン設定がされています。 / 設定を確認してください。 | The same button is assigned to multiple functions. / Please check your configuration. | The same button is set in several / places. Please check the settings. | too wide for provisional box (ERRO)
menu3077#53 | エステバリス 砲戦Ｐ | Aestivalis Artillery P | Aestivalis Arty P | too wide for provisional box (ERRO); 砲戦 = Artillery (menu3000#77 "Aestivalis Artillery Frame"); P kept as in JP

## Blocked: menu3077#54 (lote xm_menu3077_01 cannot be applied until this is decided)

`エステバリス（アカツキ）` = "Aestivalis (Akatsuki)" is 206 px; box 185 px. The validator requires both glossary names in full
("Aestivalis" 96 px + "Akatsuki" 88 px = 184 px before any space or bracket), so no faithful English can pass. Nothing was
put in the JSON for this row. Options for the owner: (a) raise the provisional width of menu3077 (the same list already
receives untested repeats from menu3000 that are much wider: #6 "Gundam Deathscythe Hell" 252 px, #36 "Aestivalis (Akito
Custom)" 251 px, #37 "Aestivalis Custom (Ryoko)" 258 px), then keep "Aestivalis (Akatsuki)"; (b) accept a glossary
exception such as "Aestivalis (Akatsu.)". I recommend (a): measure the real box.

## Recurring labels (JP -> EN) used in these screens

JP | EN | note
---|---|---
選択：㊤㊦ | Select: ㊤㊦ |
決定：○ | OK: ○ | approved common#7, hud3013#24, menu3069#1 (tm). menu3013#0 (other reviewer) still says "Confirm"
設定：㊧㊨ | Set: ㊧㊨ |
戻る：× | Back: × |
メニューに戻る：× | Return to Menu: × | like hud3013 "Return to Game"
再生：○ / 停止：× | Play: ○ / Stop: × |
item separator in help lines | the JP's own separator: 　 (ideographic) or one ASCII space where the JP has one (menu3065#0/#1) |
〜：　 (value follows) | "Label:" + 　 | menu3065#46-52, #75
ＯＮ / ＯＦＦ | ON / OFF |
初期設定に戻す | Reset to Defaults | menu3070#8 (repeated in 3071-3076)
初期設定に戻します | Reset to default settings | menu3070#31
㍉初期設定確認 | ㍉Initial Settings Confirmation | shared by new-game and reset dialogs
㍉〜確認 | ㍉<X> Confirmation | as menu3013#118 "㍉Unit Admission Confirmation"
難易度 | Difficulty | ルーキー Rookie / パイロット Pilot / エース Ace
コントローラ(タイプ) | Controller (Type) |
セレクトタイプ / シフトタイプ | Select Type / Shift Type |
セレクトメニュー / シフトメニュー | Select Menu / Shift Menu | GLOSSARIO Shift Menu
イージー / フライト (+リバース) | Easy / Flight / Easy Reverse / Flight Reverse |
簡易操作 / ピッチ／ロール | Simple / Pitch/Roll | flight help texts
リバース | Reverse (flight); Invert (camera options) | camera labels kept as translated: Invert Y-Axis / Invert
自動高度調整 | Auto Altitude Adjustment |
クイックターン | Quick Turn |
バイブレーション / 振動機能 | Vibration |
キーアサイン / キーコンフィグ | Key Assign / Key Config |
ロックサイト | Lock Sight |
ロックインフォ | Lock Info |
攻撃デモ | Attack Demo ("attack cinematics" in help) |
通信メッセージ / 通信ログ | comm messages / Comm Log | menu3004 "Comm Log"
編入 | admission / joined | menu3013 "Unit Admission"
特殊強化 | Special Upgrade (Sp. Upgrade where width forces) | menu3013#65
進化 | Evolution | menu3013#57
リミッター解除 | Limiter Release | menu3013#79
閲覧 / 事典 | Viewer / Encyclopedia | menu3004
フリーミッション / 対戦 / ＣＯＭ対戦 | Free Mission / VS Battle / COM Battle |
エースポイント | Ace Points |
お気に入りタイトル | Favorite Title |
マッフ (unit suffix) | MAFFU | GLOSSARIO Falguen MAFFU
〜艦 (named ship) | <Name> Ship / Vrlitwhai's Ship (glossary) |

## Doubts (not changed, or changed with low certainty)

1. **Provisional widths are very tight** (they are the widest JP line, ~1 EN char per JP char for lists). Many fixes are
   abbreviations only because of that: menu3062 "Chaff Gren.", "Sub Cann. 01-05", "Hvy Attacker", **"Multi-Turret"** (多砲塔戦車,
   "Tank" dropped: no form with Tank fits 136 px; restore "Multi-Turret Tank" if the box is wider); menu3061 "Calvary T.
   (Quwasan)", "S. Gan Dolla (Guntzer)", "Gilgazamune Dorchenov" (no brackets), **"Queadluun-Rau (Mass)"** (量産; preferred
   "Queadluun-Rau (Mass Production)"); menu3063 "Std. Ship (Zentran/Meltran)" (標準戦艦 = standard battleship), "Picket
   (Zentran/Meltran)", "Meltran Milia Ship", "Lg. Patrol Airlifter"; menu3069 "%s Sp. Upgrade available" (%s is a unit name,
   so the real line will be wider anyway). If the real boxes are measured wider, these should go back to the full forms.
2. **Width of repeated rows is not checked on the reusing screen**: menu3065#2 (now 301 px) is reused by menu3068#11 (box 240);
   menu3077 receives repeats from menu3000 up to 258 px (see Blocked).
3. **Name spellings with no source** (kept as the translator wrote them): スラッシュ "Thrash" (menu3063#12; also "Thrash" in
   menu3057#41/#57; the plain reading is "Slash"), グラビウス "Clavius" (menu3063#16; the JP has グ, a literal reading is
   "Gravius"), トランスポーター クォート "Transporter Quoht" ("Quoht" looks invented; "Quart"/"Quort"?), ブラネットボンバー レイ
   "Planet Bomber Ray" (JP spells ブラ-), グルグル "Guru Guru", ターナ "Tarna", ムヅラ "Muzura", リスニル "Lisnil", タントール
   "Tantor", スコル "Skoll", ハーラル "Harald", ゲター "Getter", タンギー "Tangie", リスタ "Rista", ギラッピー "Girappi", テスカスタム
   "Tes Custom", カトンボ "Katombo" (often "Katonbo"), ガンツァー "Guntzer" (ガン is "Gan" in Stark Gan Dolla; "Gantzer" would be
   consistent). Worth adding to the glossary once checked.
4. **ヤテンコウ -> "Yatenko"** follows GLOSSARIO (夜天光 = Yatenko). menu3000#54 (other reviewer) still has "Yatenkou" and
   menu3077#41 copies it; the validator accepts both because "yatenko" is a substring of "Yatenkou". One spelling should win.
5. **ゲバイ（ＳＰ） / ゲバイ・マッフ（ＳＰ）** kept with brackets "Gwei (SP)" / "Gwei MAFFU (SP)" as in the JP; GLOSSARIO has
   ゲバイSP = "Gwei SP" (unit_names #27) without brackets.
6. **menu3065#0/#1**: the JP has an ASCII space between ㊤㊦ and 決定 and an ideographic space after ○; I kept that
   (single ASCII space, then 　). Use 　 in both places if the owner prefers uniform spacing.
7. **Approved files still contain double ASCII spaces in help lines** (menu3010#0 "Exit: ⑪  Skip: ○", hud3013#24 and #26);
   the current validator would reject them. Other reviewers' menu3013#0 still uses "Confirm" for 決定.
8. **menu3072**: ＶＦＸボリューム kept as "VFX Volume" (help #17 says it is the voice volume). menu3018#21 (other reviewer)
   renders 機動戦艦ナデシコ as "Mobile Battleship Nadesico" while menu3022#6/menu3072 use "Martian Successor Nadesico" for
   the series title; one form should be chosen.
9. **menu3065#68/#72**: the JP order "forward/back = up/down" (normal) and "down/up" (reverse) was kept literally; check
   in game that Flight (normal) really climbs on stick forward.
10. **menu3076#29/#30**: 上昇回避/下降回避 rendered "evade up/down" (no fixed term found in the corpus).
