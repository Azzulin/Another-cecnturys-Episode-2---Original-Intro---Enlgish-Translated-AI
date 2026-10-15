# Meaning review: group xa (extra missions m6005-m6010), lotes xa_01..xa_06

Proposals: `rev_xa.json` (76 rows). `check_fixes.py`: 0 proposed lines with errors. All 6 **ERRO** rows of the
validation reports are covered (m6005#2; m6007#3, #4, #6; m6008#6, #39). Nothing under D:\Ace 2 was modified.

## Summary per table (for the INDICE)

Common to all six tables: no speaker labels. `<cs(1)>` marks the opposing speaker (UCE broadcast, Jonathan, Zechs,
Gablae's men, Reclaimers) and `<cs(2)>` the allied one (Yuu, Relena, the UCE agents). Besides the story lines, each
table has blocks of 8-10 interchangeable "advice/praise" lines, one per partner voice (female, male, polite,
energetic, ..., a **computer voice in katakana okurigana**, slot 7, e.g. "バリア展開中ノターゲット停止ヲ確認"), plus
continuation rows for the same voices. Gender of these voices is unknown; the EN is neutral.

- **m6005, Sanc Kingdom air defense.** Coastal AA guns hold off enemy bombers; the player guards them while the
  Gran-Garan defends out at sea. The enemy is an OZ Mobile Doll unit (barrier: they stop moving while it is up). A
  UCE broadcast on the open frequency accuses the Sanc Kingdom of harboring defectors under the pretext of refugee
  relief, of becoming a breeding ground for criminals and of ignoring repeated warnings, and threatens "the same ruin
  as before". An ally comments that war-weary people support the Sanc Kingdom, enough for the UCE to feel threatened.
  Relena demands a ceasefire ("force will solve nothing"). Failure: AA units wiped out, bombers reach the kingdom
  ("Lady Relena...!").
- **m6006, underwater recovery with the Gran-Garan.** Ciela, cooperating with the UCE to pursue Drake, introduces
  herself and keeps the Reclaimers busy. A tactical officer explains the sonar search (pings speed up near the
  target), the transmitter and the recovery boat; the cargo is vital military material of unknown nature. Yuu and
  Jonathan argue (Yuu quits Orphan's work because the Reclaimers sided with Poseidal; "Orphan's eternity is
  humanity's eternity"). The recovery boat is hit, a high energy reading appears and the cargo turns out to be an
  **Organic Plate** ("What on earth is it that we have been pursuing..."). Hazards: underwater speed loss,
  unexploded ordnance.
- **m6007, Nadesico B with the Ra Cailum.** Ruri Hoshino, captain of the Nadesico B (United Earth Space Force),
  greets the Ra Cailum; Bright Noa asks her to lead the operation. An advance team storms a base, so the Gravity
  Blast cannot be used; everyone not assaulting the base escorts the Nadesico B through the enemy lines (also
  snipers at long range). A shuttle launches before they arrive: "it" has not only fallen into Giganos hands but
  gone up into space (Bright). Ruri orders the withdrawal. Failure: Nadesico B sunk.
- **m6008, White Fang / Tallgeese.** The Ra Cailum detects White Fang. Zechs, now leader of White Fang, apologizes
  for using the UCE operation and claims the **E2**; the UCE encirclement fails. Noin begs him to stop; Zechs says
  people must be taught the folly of war and that ideals require force. Relena arrives in a civilian craft,
  introduces herself to Captain Bright and goes to stop her brother. Zechs, beaten ("the limit of a flesh-and-blood
  pilot"), praises her, asks her to forget her unworthy brother and leaves. Second part: UCE intelligence agents who
  had infiltrated White Fang flee in stolen Aries whose IFF reads as enemy; each carries the intel, one survivor is
  enough. Failure: allied Aries destroyed.
- **m6009, Grados satellites.** Grados plans to use satellites to attack Earth's major cities; three must be
  destroyed before they are ready. Major Sally Po (Peacemillion) joins Bright. Titans units appear and attack. Eiji
  begs "ゲイル先輩" (Gale, Grados officer) to stop and then bids him farewell. The female ally (probably Sally)
  thanks the Ra Cailum pilots. Voice blocks: target data sent, "your first space battle", strong enemy.
- **m6010, shuttle launch defense.** The force (Gran-Garan with an Earth commander) must protect a shuttle until
  launch; radar sites keep the AA guns working. The attackers are Gablae's men, a delaying action: Gablae is
  probably already in space. Reclaimers arrive looking for the plate born from Orphan (Organic Plate, source of the
  Antibodies); Ciela orders to fight only those who interfere. Countdown, the shuttle leaves the atmosphere; Ciela
  stays to continue the pursuit on the ground and the commander thanks "Queen Ciela Lapana" and also heads for
  space. Final phase: Giganos forces detected. Failure: shuttle destroyed.

## Fixes (ref | JP | old EN | new EN | reason)

### xa_01 (80 rows reviewed, 10 fixes)

- m6005#2 | 沿岸の対空砲が敵の爆撃機を足止めしている / 対空砲を護衛し、爆撃機の侵入を防ぐ | Coastal AA guns hold the enemy bombers. / Protect the guns and block the bombers! | Coastal AA holds off enemy bombers. / Guard the guns, keep the bombers out! | ERRO width; also "hold" -> "holds off" (足止め = stall/hold off) **[ERRO]**
- m6005#3 | グラン・ガランは外洋にて防衛します | The Gran-Garan will defend the open sea. | The Gran-Garan will defend out at sea. | 外洋にて = location (defend out at sea), not defending the sea itself
- m6005#20 | どうあっても潰す気か…！ | They will crush it no matter what... | So they mean to crush it no matter what...! | 気か = realization of intent ("so they mean to"), not a prediction; "!" restored
- m6005#28 | 敵は撤退を開始したようです | The enemy has begun to withdraw. | The enemy appears to be withdrawing. | hedge ようです lost
- m6005#44 | 次々と攻撃をすれば、敵を防げそうね | If we attack relentlessly, / we can stop the enemy! | If we keep attacking one by one, / we should be able to stop the enemy! | hedge 防げそう lost ("we can" -> "we should be able to")
- m6006#1 | 機密物資の破壊 | Destroy the classified supplies | Destruction of the classified supplies | FAILURE condition (cargo must be recovered intact, cf. #13 "handle with extreme care"); EN was an order to destroy it. Style as approved m6043#1 "Sinking of the Albion"
- m6006#4 | ドレイクを追うためＵＣＥに協力している | To pursue Drake, / I am cooperating with the UCE. | Cooperating with the UCE to pursue Drake, | <ab(0)> relative clause running into #5 ("..., I am Ciela Lapana of the Gran-Garan"); EN closed the sentence
- m6006#18 | オルファンがやろうとしていることを邪魔する奴は | Anyone who gets in the way of / what Orphan is trying to do... | Anyone who gets in the way of / what Orphan is trying to do | <ab(0)> continuation: EN closed the sentence with "..."
- m6006#19 | 全て排除する | I will eliminate every last one! | will be eliminated, every last one! | continues #18 as one sentence
- m6006#21 | 今は違う。グランチャーの任務も | It's different now! / The Grand Cher's mission, | It's different now! / The Grand Chers' mission | grammar: stray comma between subject and verb across #21/#22

### xa_02 (80 rows reviewed, 14 fixes)

- m6006#23 | 貴様は覚悟が足りないから、 | Because you lack resolve, / you try to run away from Orphan! | It's because you've got no resolve | MISALIGNED: #23 carried the content of #24 too; now one sentence over #23/#24
- m6006#24 | オルファンから逃げ出そうとかするんだよ！ | You coward! You are not even a man!! | that you try to run away from Orphan! | MISALIGNED: carried the content of #25 (duplicate "You coward..."); now its own JP
- m6006#25 | いくじなしめ！　男じゃないんだよ！！ | You coward! You are no man at all!! | You coward! You're no man at all!! | Jonathan voice (contractions)
- m6006#26 | 言ったな…ジョナサン・グレーン！ | Now you have said it... Jonathan Glenn! | Now you've said it... Jonathan Glenn! | Yuu voice (contraction)
- m6006#30 | ポセイダルなんて奴らと手まで組んで、 | Teaming up with people like Poseidal... | Even teaming up with the likes of Poseidal, | <ab(0)> continuation closed with "..."; まで (even) restored
- m6006#31 | そんなことを手伝う仕事なんか、もう嫌だ | I want no part in helping with that! | I'm sick of any job that helps with that! | もう嫌だ = fed up ("sick of"), not "I want no part"
- m6006#33 | それがわからないのかよ | Can you not understand that? | Can't you understand that? | Jonathan casual よ: contraction
- m6006#35 | どこへ行く、ジョナサン・グレーン！ | Where are you going, Jonathan Glenn! | Where are you going, Jonathan Glenn?! | question mark lost
- m6006#56 | アラームメッセージ、海中デノ速度低下ヲ確認 | Alarm: speed reduction underwater. | Alarm message: underwater speed loss confirmed. | glossary term "Alarm message"; 確認 dropped
- m6006#65 | ソナー音間隔上昇方向ニ、ターゲットヲ確認 | Target confirmed where sonar interval rises. | Target confirmed toward faster sonar pings. | "sonar interval rises" means SLOWER pings, the opposite of the mechanic (#9: closer = faster)
- m6007#3 | 連合宇宙軍より派遣されている / ナデシコＢ艦長のホシノ・ルリです | From the United Earth Space Force, / I am Ruri Hoshino, captain of Nadesico B. | I'm Ruri Hoshino, Nadesico B captain, / sent by the United Earth Space Force. | ERRO width; compacted, nothing cut **[ERRO]**
- m6007#4 | ラー・カイラム艦長、ブライト・ノアです / 作戦の主導をお願いします | I am Bright Noa, captain of the Ra Cailum. / Please take the lead in this operation. | This is Bright Noa, Ra Cailum captain. / Please take the lead in this operation. | ERRO width; compacted **[ERRO]**
- m6007#6 | 現在、既に先発隊が基地へ進攻中です / ヘタにグラビティブラストは撃てません | An advance team is already inside the base. / We cannot fire the Gravity Blast blindly. | An advance team is storming the base. / We can't risk firing the Gravity Blast. | ERRO width; 進攻中 = attacking, not "inside"; ヘタに = rashly ("can't risk") **[ERRO]**
- m6007#8 | 結構ピンチで時間もないので、よろしく | We are in a pinch and out of time. / We are counting on you. | We're in quite a pinch and short on time, / so we're counting on you. | 時間もない = short on time ("out of time" = already too late); 結構 = quite

### xa_03 (80 rows reviewed, 9 fixes)

- m6007#41 | ナデシコＢヲ護衛セヨ | DEFEND NADESICO B. | Escort the Nadesico B. | all-caps computer voice -> sentence case (approved Rei line m6194#85 "Alarm message. Pursuit from rear." and accepted fix m6007#32); 護衛 = escort
- m6007#51 | 遠距離ニターゲットヲ確認 | TARGET CONFIRMED AT LONG RANGE. | Target confirmed at long range. | all-caps -> sentence case
- m6007#57 | 可能な限り撃破してください | Please destroy them as much as possible. | Please destroy as many as possible. | "destroy them as much as possible" -> "as many as possible"
- m6007#61 | 可能ナ限リ、即時撃破セヨ | DESTROY IMMEDIATELY IF POSSIBLE. | Destroy at once, as far as possible. | all-caps -> sentence case
- m6008#2 | 友軍エアリーズの撃破 | Defeat allied Aries | Destruction of allied Aries | FAILURE condition (the allied Aries carry the UCE agents, #47-52); EN was an order to destroy allies
- m6008#6 | そちらの作戦に便乗したことは詫びよう / だが、Ｅ２は我々がいただく！ | My apologies for taking advantage of your op. / However, the E2 belongs to us! | I apologize for using your operation. / However, we will be taking the E2! | ERRO width; いただく = "we will take", not "belongs to us" **[ERRO]**
- m6008#16 | 何故、このようなことをするのです！ | Why must you do such a thing! | Why are you doing such a thing?! | "must" added; question mark
- m6008#35 | お前ならきっと、父上の理想とした国を / 導いてゆけるはずだ | You will surely guide the nation / our father envisioned. | Surely you can lead the nation / that our father envisioned. | きっと...はず = "surely you can", not a prediction
- m6008#39 | 複数の機影の接近を確認 / これは…我が軍の救難信号です！ | Multiple contacts approaching confirmed. / This is... our forces' distress signal! | Confirming multiple contacts inbound. / This is... our forces' distress signal! | ERRO width; compacted **[ERRO]**

### xa_04 (80 rows reviewed, 18 fixes)

- m6008#41 | 潜入していたホワイトファングより | We infiltrated White Fang, | We had infiltrated White Fang | tense/sense: they had infiltrated White Fang and escaped from it
- m6008#42 | 混乱に乗じて脱出したが、追撃されている | and escaped amid confusion, but are pursued. | and escaped in the confusion, but we're being pursued. | grammar ("but are pursued")
- m6008#44 | 入手した情報はそれぞれが所持している | Each of us carries parts of the Intel obtained. | Each of us carries the intel we obtained. | "parts of the Intel" invented (contradicts #45: one survivor is enough) and wrong capital
- m6008#62 | やだ、こいつ強いじゃない！ | Damn it, this one is strong! | No way, this one's strong! | やだ = "no way/ugh"; "Damn it" invented curse
- m6008#64 | アラームメッセージ、ダメージ拡大 | ALARM: DAMAGE EXPANDING. | Alarm message: damage spreading. | glossary "Alarm message"; all-caps -> sentence case
- m6008#66 | 敵の性能は相当のものよ、注意して | The enemy's performance is substantial, watch out. | The enemy's performance is formidable, be careful. | "performance is substantial" unidiomatic -> formidable
- m6008#76 | 攻撃回避を推奨します | EVASION RECOMMENDED. | Evasive action is recommended. | not the computer voice (plain 推奨します = formal voice, slot 9 of 9); all-caps removed
- m6008#77 | 動きをよく見れば、味方の区別はつくはずよ | Watch their movement closely, you can tell allies apart. | Watch their movement closely and you / should be able to spot the allies. | hedge はず lost; comma splice
- m6008#80 | 動きを見れば、味方の区別はつくはずよ | If you watch how they move, you can distinguish them. | Watch how they move and you should be / able to tell the allies apart. | hedge はず lost
- m6008#81 | ちゃんと動きを見れば味方がわかるわよ | Look closely at their movement and you will know allies. | Look closely at how they move and / you'll know which ones are allies. | "you will know allies" ungrammatical
- m6008#83 | 破壊目標ト護衛目標ノ動キニ、誤差ヲ確認 | MOVEMENT DISCREPANCY NOTED BETWEEN TARGET AND ALLY. | Discrepancy confirmed in movement of / destroy targets and escort targets. | all-caps -> sentence case; 破壊目標/護衛目標 kept
- m6008#85 | 動きをよく見れば区別はつくはずよ | If you watch their movement closely, you can tell. | Watch their movements closely and / you should be able to tell. | hedge はず lost
- m6008#56 | 複数の機影の接近を確認 | Multiple contacts approaching confirmed. | Confirming multiple contacts inbound. | same JP as #39 line 1, kept consistent
- m6009#0 | 衛星３基及び敵勢力の撃破 | Destroy 3 Satellites and Enemy Forces | Destroy 3 satellites and enemy forces | objective title case -> sentence case like the other objectives
- m6009#5 | 準備が整う前に何としても止めなくては | We must stop them before preparations finish! | We must stop them at all costs / before their preparations are complete! | 何としても (at all costs) dropped
- m6009#17 | 私はピースミリオンを任されている | I have been entrusted with the Peacemillion. | Entrusted with the Peacemillion, | <ab(0)> relative clause running into #18 ("Entrusted with the Peacemillion, I am Major Sally Po.")
- m6009#33 | 目標の位置情報を送ったから、 | Sent the target location data, so | I sent you the target location data, | から、 continues into #43 (same voice)
- m6009#35 | 目標ノ位置情報ヲ表示 | DISPLAYING TARGET POSITION DATA. | Displaying target position data. | all-caps -> sentence case

### xa_05 (80 rows reviewed, 16 fixes)

- m6009#43 | それを見て、どんどん破壊しちゃって！ | Watch that and destroy them one after another! | so check it and wreck them one after another! | continues #33 (", so check it and..."), lowercase
- m6009#45 | 至急、目標ノ撃破ニ向カエ | PROCEED TO DESTROY TARGET IMMEDIATELY. | Proceed to destroy targets at once. | all-caps -> sentence case
- m6009#48 | 表示に従い、目標の撃破に向かってください | Follow display and proceed to destroy target. | Please follow the display and proceed / to destroy the targets. | telegraphic "Follow display..." for the polite formal voice (ください)
- m6009#50 | 宇宙戦は初めてだが、油断しないように | This is your first space battle, do not drop guard. | It's your first space battle, / so don't let your guard down. | "do not drop guard" ungrammatical
- m6009#53 | 宇宙戦だけど大丈夫よね、応援してるわ！ | It is a space battle, but you will do great, rooting for you! | It's a space battle, but you'll be fine, / right? I'm rooting for you! | 大丈夫よね = "you'll be fine, right?"; run-on
- m6009#61 | やだ、こいつ強いじゃない！ | Damn it, this one is strong! | No way, this one's strong! | same as m6008#62 ("Damn it" invented)
- m6009#63 | アラームメッセージ、危険、回避セヨ | ALARM: DANGER, EVADE IMMEDIATELY. | Alarm message: danger. Evade. | glossary "Alarm message"; "immediately" added; all-caps
- m6009#65 | 敵の性能は相当のものよ、注意して | The enemy's performance is substantial, take care. | The enemy's performance is formidable, take care. | same as m6008#66
- m6010#0 | 一定時間のシャトル防衛 | Defend Shuttle for a Set Time | Defend the shuttle for a set time | missing article; title case
- m6010#1 | シャトルの破壊 | Destruction of Shuttle | Destruction of the shuttle | missing article (failure condition, style "Sinking of the Albion")
- m6010#3 | この機を逃せば打ち上げは難しい | If we miss this chance, launch will be impossible. | If we miss this chance, a launch will be difficult. | 難しい = difficult, not impossible
- m6010#35 | 打ち上げ１０秒前、 | 10 seconds to launch. | 10 seconds to launch, | JP comma: the countdown continues in #36
- m6010#36 | ９、８、７、６、５、４、３、２、発射！ | 9, 8, 7, 6, 5, 4, 3, 2, ignition! | 9, 8, 7, 6, 5, 4, 3, 2, liftoff! | 発射 = launch/liftoff, not ignition
- m6010#39 | よくやってくれました | You have done exceedingly well. | You have done well. | "exceedingly" added (same JP as m6006#29 "You have done well.")
- m6010#41 | 宇宙でのご活躍、期待しております | I anticipate your glorious success in space. | I look forward to your success in space. | "glorious" added
- m6010#43 | 我々も宇宙へ上がるぞ | We too shall ascend to space. | We're heading up into space as well. | shuttle-side commander (probably Bright, curt): "shall ascend" too archaic

### xa_06 (40 rows reviewed, 9 fixes)

- m6010#56 | 最終防衛ライン、レディ | FINAL DEFENSE LINE, READY. | Final defense line, ready. | all-caps -> sentence case (computer-voice slot 7)
- m6010#60 | 突破してきた敵からシャトルを守って | Protect the shuttle from penetrating hostiles. | Protect the shuttle from any enemies / that break through. | "penetrating hostiles" unclear
- m6010#64 | シャトルぐらい、敵から守ってよね | You can at least protect the shuttle from enemies. | At least keep the shuttle safe / from the enemy, okay? | ぐらい...守ってよね is a plea ("at least keep it safe, okay?"), not a statement
- m6010#66 | シャトルノ撃破ヲ回避セヨ | PREVENT DESTRUCTION OF SHUTTLE. | Prevent destruction of the shuttle. | all-caps -> sentence case
- m6010#70 | シャトルが危ないわ！　近づけさせないで！ | The shuttle is in danger! Do not let them close! | The shuttle is in danger! Don't let them get close! | "Do not let them close" ungrammatical
- m6010#76 | アラームメッセージ、シャトルノ損傷拡大 | ALARM: SHUTTLE DAMAGE EXPANDING. | Alarm message: shuttle damage spreading. | glossary "Alarm message"; all-caps
- m6010#77 | シャトルの損傷拡大、このままでは危険です | Shuttle damage expanding, it is critical at this rate. | Shuttle damage spreading. At this rate, / it will be in danger. | 危険 = in danger, not "critical"
- m6010#83 | レーダーはなるべく壊されないようにね | Try not to get radar wrecked as much as you can. | Do your best not to let the radars get wrecked. | "get radar wrecked as much as you can" reads as the opposite order
- m6010#86 | 可能ナ範囲デレーダーヲ防衛セヨ | DEFEND RADAR TO EXTENT POSSIBLE. | Defend the radar to the extent possible. | all-caps -> sentence case

## Doubts not changed (for the project owner)

1. **"Senior Gale"** (m6009#22, #24, ゲイル先輩): awkward English. The approved story ops use "Senpai" (m6211#42,
   m6214#21/#24, Hikaru to Focker), which conflicts with the no-romanized-honorifics rule. Options: plain "Gale"
   (my preference), "Senpai", or keep "Senior Gale". Left as is until a project-wide decision on 先輩.
2. **制圧 = "suppress"** (m6007#26-35, "suppress the base", "base suppression op"): understandable but unidiomatic;
   "take/secure the base" would be more natural. Ten voice lines plus the accepted fix m6007#32 use it, so left
   for consistency. Check what the story ops use for 基地制圧.
3. **m6007#6** "An advance team is storming the base.": 既に (already) dropped to fit the width ERRO; the
   progressive keeps "now". Any longer wording fails at 380 px.
4. **Failure-condition style**: approved m6043#1 "Sinking of the Albion" is a noun phrase, so I used "Destruction
   of ..." for m6006#1, m6008#2, m6010#1. m6005#1 "All air defense units destroyed" and m6007#1 "Sinking of the
   Nadesico B" were left. That m6006#1 (機密物資の破壊) is a failure condition is my inference from the dialogue
   (#12-13, recovery mission); not visible in the data.
5. **Speakers not identified** (kept neutral): m6005#4-7, #9, #12-13, #20-23 (Sanc-side ally; plain male-ish
   だ/な); m6006#8-13 (tactical officer, くれ); m6006#41-42, #46 ("Captain" and the commander answering, which ship
   is unknown); m6006#47-48 ("この輝きは…何故、このようなものが…", maybe Ciela); m6008#5, #8, #14, #28-29 (most
   likely Bright); m6009#3-5, #10-12, #27-28 (female ally, probably Sally Po); m6010#3-5, #19-21 (formal, maybe
   Ciela), #29-30, #42-43 (Earth commander, probably Bright). m6007#10-12 and #14 read as Ruri.
6. **m6008#53** (`<cs(1)>`, "見つかったか！ 逃げろ！"): `<cs(1)>` is the opposing side elsewhere, but the line fits
   the fleeing agents better. EN "They found us! Run!" works for either; left.
7. **m6007#19** "it" (what fell into Giganos hands and went to space) is never named in the table. Left vague as
   in the JP.
8. **m6005#16** 亡命者 rendered "defectors"; "exiles/asylum seekers" also possible. Left.
9. **m6008#19** "Exercising power is necessary for our ideals.": "our" is not in the JP (理想のためには); minor, left.
10. **Translator notes** call the katakana voice "Rei" (Layzner computer). Nothing in these tables confirms who it
    is; not used in the EN.

## Glossary / speaker problems

- Missing from GLOSSARIO (translator made no proposals): サリィ・ポォ = **Sally Po** (female, Gundam Wing, Major),
  ピースミリオン = **Peacemillion** (ship), ゲイル = **Gale** (Ahmos Gale, Layzner, male; his unit Grimekaisar is in
  the glossary), ティターンズ = **Titans** (faction, Zeta Gundam: not in the series list of the project),
  モビルドール = **Mobile Doll** (term), サンクキングダム = **Sanc Kingdom** (place), Ｅ２ in m6008#6 (exists as
  Ｅ２物質/Ｅ２コア; "E2" used).
- アラームメッセージ is a glossary term ("Alarm message"). The translator wrote "Alarm:" / "ALARM:" in four rows; fixed
  (m6006#56, m6008#64, m6009#63, m6010#76).
- **All-caps**: the translator wrote the computer voice in capitals from xa_03 on and lowercase in xa_01/02. The
  approved Rei line m6194#85 and the accepted fix m6007#32 use sentence case, so all of them are normalized
  (m6007#41, #51, #61; m6008#64, #83; m6009#35, #45, #63; m6010#56, #66, #76, #86). m6008#76 (攻撃回避を推奨します)
  was capitalized by mistake: it is the formal voice, not the computer one.
- Relena introduces herself as "リリーナ・ピースクラフト" (m6008#24): "Relena Peacecraft" is correct there, even though
  the glossary's full_name is Relena Darlian.
- Poseidal is **female** in the glossary. m6006#30 "the likes of Poseidal" has no pronoun, OK.
