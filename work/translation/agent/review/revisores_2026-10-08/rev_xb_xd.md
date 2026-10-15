# Revisão xb (tutorial) e xd (missões curtas/sistema)

Rows reviewed: xb_01 80, xb_02 80, xb_03 80, xb_04 75, xd_01 80, xd_02 2 (397). Fixes: xb_01 24, xb_02 49, xb_03 20,
xb_04 4, xd_01 10, xd_02 0 (107). All **ERRO** rows covered (23/33/16/0/1/0); check_fixes.py: 0 errors, 0 warnings.
BASE_RULES.md (D:\Ace 1\...) is not on this machine; PLANO.md + the task rules were used.

## What the tables contain (for INDICE)

- **m6302 / m6303 (xb)**: the in-game tutorial played in the practice/training missions. Voice: the training program
  itself ("演習プログラム起動。" / "以上で説明を終了します。"), an impersonal polite system narrator (です/ます, ～しましょう),
  not a cast member; English in a neutral instructive "you" register. Rows #0-191 (+#312-313) explain one function per
  block (Thruster, Glider, Roller Dash, Transformation, additional armor/Purge, Charge, Multi-Lock, combo branching,
  Multi-Shot, missile interception, Counter Slash, Wire/Hold attacks, thrown weapons, Brain Powerd mood, V-MAX, Beam
  Coating, Vital Jump, Boson Jump, God Shadow, GP03 controls, Winger Binder, claw arm, Aura Power, God Gundam Hyper
  Mode/Meikyo Shisui, Chaff, Aura Barrier, Chakra Shield, Distortion Field, Valkyrie 3-stage transformation, Slit
  Wafer, Guardian Cannon, Wings of Rean, Trans Unit, Funnels, Active Cloak, Bio-Relation, I-Field, Dummy Balloon,
  Hyper Jammer). Rows #192-311 are "Weapon N: name" / "Ability: name" labels: per-unit lists of the weapons that have
  the function being explained (original-id order: Dunbine family, L-Gaim/A.Taul, Layzner/Daljan, Dragonar, Brain
  Powerd, Aestivalis, Wing Gundams, Nu Gundam/Sazabi/Re-GZ, GP03, Neue Ziel, Valkyries, God Gundam, Nanajin, Gun Ark,
  Buster Ark). m6303 is a copy of m6302 (differs only in #232 キャバリア, #273, #276). Many rows are reused by several
  blocks (e.g. #27, #30, #33-35, #71-73, #99, #135, #138, #165-167), so they must stay generic.
- **xd**: m6340-m6361 = one-line victory conditions of the extra/versus duels ("Defeat <unit>"); m6900 (= m6903) =
  an unused/extra mission with the Ra Cailum (storage depots, Drake's Will Wipps ambush, Sector E) plus a few Zechs/
  Relena lines from Endless Waltz (#53-56); m6905 = Endless Waltz extra objectives + two Amuro lines; m6901 and m6998
  = developer test strings ("バストアップ テスト", kanji font test, "ロンドベルは鈴を鳴らし①-⑤").

## System terms settled (JP -> EN)

| JP | EN |
|---|---|
| 搭乗ユニット / 現在の搭乗ユニット | the unit you are piloting / your currently piloted unit |
| 機体 | unit |
| ウェポン / アビリティ | Weapon / Ability (labels "Weapon 2: ...", "Ability: ...", as hud3020) |
| スラスター / グライダー / ローラーダッシュ | Thruster / Glider / Roller Dash |
| ダッシュ / ダッシュボタン / ダッシュターン | Dash / Dash button / Dash Turn |
| バーニア / バーニアゲージ | vernier / vernier gauge |
| 変形操作 / 戦闘機形態 / 通常形態 | transform action / Fighter mode / Normal mode |
| 戦闘機操作(タイプ) | fighter controls / fighter control type (Options) |
| 追加装甲 / アーマー | additional armor / Armor (the HP stat) |
| パージ / パージ操作 | Purge / Purge command |
| チャージ攻撃 | Charge Attack (charge) |
| マルチロック / マルチショット | Multi-Lock / Multi-Shot |
| 連続攻撃 | combo attack |
| 斬り返し | Counter Slash |
| ワイヤー攻撃 / ホールド攻撃 | Wire Attack / Hold Attack |
| メインウェポンボタン / 近接攻撃 | main weapon button / Melee |
| 攻撃ボタン / 発動ボタン | attack button / activation button |
| 回避操作 / 射出操作 | evade command / launch |
| チェイン | Chain |
| 必殺技 | special finisher |
| 明鏡止水(モード) / ハイパーモード | Meikyo Shisui (Mode) / Hyper Mode |
| 昇順変形 / 降順変形 | Ascending / Descending Transform |
| ３段変形 / 三段変形 | 3-Stage Transformation |
| ウィンゲルバインダー / バインダー | Winger Binder / binder |
| クローアーム / 有線クローアーム | Claw Arm / Wired Claw Arm |
| 支援砲撃 / ガーディアン砲 | support fire / Guardian Cannon |
| 機嫌 | mood |
| 拡散 (weapon names) | Diffuse |
| 〜変形 (weapon labels) | "X Transform" (kept the translator's pattern) |
| 出撃 | sortie |
| ～の撃破 / ～の全撃破 / ～に勝利 (objectives) | Destroy the X / Destroy all X / Defeat X (sentence case, as m60xx) |
| 撃沈 / 逃走 / 撤退 | Sink / escape / retreat |

## Fixes (ref | JP | old EN | new EN | reason)

### xb_01 (24 fixes)

- m6302#1 | 搭乗ユニットに搭載されている / 特殊機能の説明を行います。 | Explaining the special functions equipped / on your currently piloted unit. | Now explaining the special functions / installed on the unit you are piloting. | width (ERRO)
- m6302#5 | スラスターは、ロック対象を機体の正面に / 捉えたままダッシュが行える機能です。 | The Thruster lets you Dash while keeping / your locked target in front of your unit. | Thruster lets you Dash while your unit / keeps the locked target in front of it. | width (ERRO)
- m6302#7 | スラスター中は対象を正面に捕捉しながら / 高速移動することが可能です。 | During Thruster use, you can move at high speed / while keeping your target locked forward. | With Thruster, you can move at high / speed while keeping the target ahead. | width (ERRO)
- m6302#11 | 特徴としては、ダッシュ中に高速の / 上昇・下降が可能なことが挙げられます。 | A key feature is the ability to rapidly climb / or dive at high speed while dashing. | Its key feature is the ability to climb / and dive at high speed while dashing. | width (ERRO); "rapidly ... at high speed" redundancy
- m6302#14 | ローラーダッシュは、バーニアを消費せずに / 地上を高速移動できる機能です。 | Roller Dash allows high-speed ground travel / without consuming vernier gauge. | Roller Dash lets you move fast on the / ground without consuming vernier. | width (ERRO)
- m6302#19 | 長距離を移動する時、遠距離にいる敵を / 強襲する時、敵との距離をとりたい時など、 | When traveling long distances, assaulting distant / enemies, or opening distance from foes, | When traveling far, raiding distant / enemies, pulling away from them, etc., | width (ERRO); keeps the "etc." (など)
- m6302#21 | 戦闘機形態の時にもう一度変形操作を行うと / 通常形態に戻ることができます。 | Performing the transform action again while in / Fighter mode returns you to Normal mode. | Transform again in Fighter mode / to return to Normal mode. | width (ERRO)
- m6302#22 | また、地面や障害物に接触すると、強制的に / 通常形態に戻るので注意してください。 | Note that colliding with terrain or obstacles / forces you back into Normal mode. | Note: touching the ground or obstacles / forces you back to Normal mode. | width (ERRO); 地面 = the ground
- m6302#28 | また、アーマーが一定量まで低下した場合も / 追加装甲は強制的にパージされます。 | Additional armor is also forcibly purged / if your Armor drops below a certain level. | Additional armor is also force-purged / if your Armor drops to a certain level. | width (ERRO)
- m6302#29 | パージ後は、武装や装甲などの機体性能が / 変化するので、注意しましょう。 | Be aware that unit specs such as weapons and / armor change after purging. | After a Purge, unit specs such as / weapons and armor change. Be careful. | width (ERRO); Purge term
- m6302#32 | また、アーマーが一定量まで低下した場合や / 地面や障害物に接触した場合でも、 | If Armor drops below a certain level or upon / colliding with terrain or obstacles, | Also, if Armor falls to a set level or / you touch the ground or an obstacle, | width (ERRO)
- m6302#36 | また、アーマーが一定まで低下した場合や / 地面や障害物に接触した場合でも、 | Also, if Armor drops below a threshold or upon / colliding with terrain or obstacles, | Also, if Armor falls to a set level or / you touch the ground or an obstacle, | width (ERRO)
- m6302#37 | 現在の搭乗ユニットは、追加装甲を / 二重に装備しているため、 | Because your currently piloted unit is equipped / with double layers of additional armor, | Since your unit is fitted with two / layers of additional armor, | width (ERRO)
- m6302#39 | 二つ目の追加装甲は、パージ操作と / アーマーの低下によってパージされます。 | The second additional armor is purged via / the Purge command or armor reduction. | The second layer is purged with the / Purge command or when Armor drops. | width (ERRO)
- m6302#43 | 攻撃ボタンを離すと、チャージ量に応じた / 出力の攻撃が発動します。 | and releasing the attack button unleashes / an attack scaled to the charge amount. | and releasing it unleashes an attack / whose output matches the charge. | width (ERRO)
- m6302#44 | チャージするほど強力な攻撃となる反面、 / チャージ中には隙が生じるので、 | While charging delivers higher attack power, / it leaves you vulnerable while charging, | The more you charge, the stronger the / attack, but charging leaves you open, | width (ERRO)
- m6302#50 | また、ウェポンによっては、一つの対象に / 対するマルチロックも可能です。 | Depending on the weapon, multi-locking onto / a single target is also possible. | Some weapons can also Multi-Lock / onto a single target. | width (ERRO)
- m6302#51 | 複数の敵との戦闘には特に有効なので、 / 積極的に使用しましょう。 | This is particularly effective against multiple enemies, / so make active use of it. | It is especially effective against / groups of enemies, so use it actively. | width (ERRO)
- m6302#58 | 攻撃した際、ロック対象付近の対象にも / 自動的に攻撃が分散します。 | When fired, attacks automatically spread to targets / near your locked target. | The attack automatically spreads to / targets near the locked target. | width (ERRO)
- m6302#60 | このウェポンには、ミサイルを迎撃する / 機能が搭載されています。 | This weapon is equipped with a function to / intercept incoming missiles. | This weapon is equipped with a / missile interception function. | width (ERRO)
- m6302#61 | ミサイルが機体正面に接近してきた時に / 使用すると、 | Using it when missiles approach from the front / of your craft | Using it when missiles close in on / the front of your unit | 機体 = unit (not "craft"); clean 2-line layout
- m6302#66 | その間に敵の近接攻撃を受けると、 / 斬り返しが成功します。 | and taking an enemy melee hit during this window / successfully triggers a counter-slash. | and if an enemy melee attack hits you / then, the Counter Slash succeeds. | width (ERRO); Counter Slash as in the label #305
- m6302#69 | ワイヤー攻撃は、対象をワイヤーで捕獲して / 様々な追加攻撃を繰り出せる機能です。 | Wire Attack ensnares a target with wire to / unleash various follow-up attacks. | Wire Attack snares a target with wire / to unleash various follow-up attacks. | width (ERRO)
- m6302#71 | その時、タイミングよくメインウェポンボタンか / 近接攻撃を入力することで、 | At that moment, pressing the Main Weapon button / or Melee button with good timing | Then, a well-timed press of the main / weapon button or a Melee input | width (ERRO); main weapon (glossary) / Melee input

### xb_02 (49 fixes)

- m6302#82 | それまでは、その武器を使うウェポンは / 使用できません。注意してください。 | weapons using that blade are unavailable / until it returns. Please take note. | until then, you can't use any Weapon / that uses it. Please take note. | width (ERRO); invented "blade" removed (the thrown melee weapon is generic)
- m6302#83 | ブレンパワードは出撃時の機嫌によって / 性能が大幅に変化します。 | A Brain Powerd's performance changes greatly / depending on its mood at sortie. | A Brain Powerd's performance varies / greatly with its mood at sortie. | width (ERRO)
- m6302#84 | 出撃時のアーマーが多い場合は、 / 機嫌が良くなる確率が上がりますが、 | Sorting with high Armor raises the chance / of starting in a good mood, but | High Armor at sortie raises the chance / of a good mood, but | typo "Sorting" (= sortie) made the line meaningless
- m6302#86 | 機嫌の良い状態でいてもらうため、 / 可能な限り休ませることを心がけてください。 | To keep them in a good mood, endeavor / to let them rest as much as possible. | To keep it in a good mood, try to let / it rest as much as possible. | width (ERRO); pronoun "it" consistent with #83 "its mood"
- m6302#87 | 機嫌は出撃前のメニュー画面で / 確認することができます。 | You can check their mood on the menu screen / prior to sortie. | You can check its mood on the menu / screen before sortie. | pronoun consistent with #83/#86
- m6302#89 | Ｖ－ＭＡＸは、ユニットの各性能を / 大幅に上昇させる機能です。 | V-MAX is a function that drastically increases / all of the unit's performance specs. | V-MAX greatly boosts all of / the unit's performance. | width (ERRO)
- m6302#90 | アーマーが一定以下になると / 発動が可能になります。 | It becomes available for activation once Armor / drops below a certain threshold. | It can be activated once Armor / falls to a certain level or below. | width (ERRO); 一定以下 = at or below a set level
- m6302#91 | 発動中は、体当たりによる強襲攻撃が / 使用できます。 | While active, you can execute a devastating / tackling assault attack. | While active, you can use a ramming / assault attack. | invented "devastating" removed
- m6302#92 | バーニアゲージが０になると解除され、 / 数秒間行動不能になるのが欠点です。 | It deactivates when Vernier Gauge reaches 0, / leaving you immobilized for several seconds. | Drawback: at 0 vernier gauge it ends / and you can't act for a few seconds. | width (ERRO); restores 欠点 (drawback); vernier gauge lowercase as glossary
- m6302#96 | ビーム系攻撃を多用する敵に対しては、 / 非常に有効な機能です。 | It is exceptionally useful against enemies / relying heavily on beam attacks. | It is very effective against enemies / that rely heavily on beam attacks. | width (ERRO)
- m6302#98 | 回避操作を行うと、姿を消した状態で / 回避を行います。 | Performing the evade action executes an evasion / while temporarily vanishing from sight. | The evade command makes the unit / vanish from sight as it evades. | width (ERRO)
- m6302#100 | ボソンジャンプは、攻撃を受けずに / 一定距離を瞬時に移動できる機能です。 | Boson Jump allows you to instantly traverse / a set distance without taking damage. | Boson Jump instantly moves you a set / distance without being hit. | width (ERRO); 攻撃を受けずに = without being hit
- m6302#102 | 敵の攻撃を回避する時、敵の懐に飛び込んで / 強襲をかける時などに利用しましょう。 | Use it to dodge incoming enemy attacks or to dive / straight into point-blank range. | Use it to dodge attacks or to dive / in close to an enemy for an assault. | width (ERRO)
- m6302#103 | ゴッドシャドーはダメージを受けずに / 回避ができる機能です。 | God Shadow allows you to evade incoming attacks / without taking damage. | God Shadow lets you evade attacks / without taking damage. | width (ERRO)
- m6302#104 | 回避操作を行った際、複数の幻影を / 作り出すことで攻撃を回避します。 | Performing the evade action generates multiple illusions / to dodge enemy attacks. | Using the evade command creates / multiple illusions to dodge attacks. | width (ERRO)
- m6302#106 | 通常移動時は、通常ユニット操作ですが、 / ダッシュ中は戦闘機操作になります。 | During normal travel it handles like standard units, / but during Dash it switches to Fighter controls. | It handles like a normal unit, but / switches to fighter controls in Dash. | width (ERRO)
- m6302#107 | ダッシュ中の戦闘機操作は、オプションの / 戦闘機操作タイプが反映されます。 | Fighter controls during Dash reflect the Fighter / Control Type chosen under Options. | Fighter controls in Dash follow the / fighter control type set in Options. | width (ERRO)
- m6302#108 | ウィンゲルバインダーは、遠隔操作による / 攻撃が可能なウェポンです。 | Wingel Binders are remotely operated weapons / capable of detached attacks. | The Winger Binder is a Weapon that / attacks by remote control. | glossary: Winger Binder (was "Wingel Binders"); "detached attacks" invented
- m6302#109 | 射出操作を行うと、両腕に装着された / ウィンゲルバインダーが射出されます。 | Triggering launch fires both Wingel Binders / mounted on the unit's arms. | Launching fires the Winger Binders / mounted on both arms. | glossary: Winger Binder
- m6302#110 | 射出されたバインダーは、攻撃ボタンを / 押すことで、対象を攻撃します。 | Pressing the attack button commands the detached / binders to assault the target. | Launched binders attack the target / when you press the attack button. | width (ERRO)
- m6302#111 | 一定時間が経過すると、バインダーは / 機体の元へ戻ります。 | After a set time elapses, the binders return / to the craft. | After a set time, the binders return / to the unit. | 機体 = unit (not "craft")
- m6302#113 | クローアームは、遠隔操作による / 攻撃が可能なウェポンです。 | The Claw Arm is a remotely operated weapon / capable of ranged deployment. | The Claw Arm is a Weapon that / attacks by remote control. | "capable of ranged deployment" invented; parallel with #108 (遠隔操作による攻撃)
- m6302#114 | 射出操作を行うと、メインアームから / クローアームが遠方に射出されます。 | Executing launch fires the Claw Arm outward / from the main arm assembly. | Launching fires the Claw Arm far out / from the main arm. | clumsy "Executing launch"; 遠方に kept
- m6302#115 | 射出されたクローアームは、攻撃ボタンを / 押すことで、対象を攻撃します。 | Pressing the attack button commands the deployed / Claw Arm to strike the target. | Press the attack button to have the / launched Claw Arm attack the target. | width (ERRO)
- m6302#117 | 射出中は、メインアームによる直接攻撃が / 使用できないので注意してください。 | Note that direct attacks with the main arm cannot / be used while the claw is launched. | Note: while it is launched, the main / arm can't make direct attacks. | width (ERRO)
- m6302#119 | オーラ力が発揮されるのは一定時間のみ / ですが、その効果は絶大です。 | Aura Power remains active for a limited time, / but its effect is tremendous. | Aura Power lasts only for a set time, / but its effect is tremendous. | width (ERRO)
- m6302#120 | 適切なタイミングで使うことで、戦闘を有利に / 進めることができるでしょう。 | Deploying it at the right moment will grant you / a major advantage in combat. | Use it at the right moment to gain / the upper hand in battle. | width (ERRO); invented "major" removed
- m6302#122 | 敵を倒した時、チェイン中の時、 / あるいはピンチに陥った時などに、 | When felling foes, maintaining chains, or when / cornered in danger, | When you defeat enemies, in a Chain, / or when you are in a pinch, | Chain = system term (HUD "Chain Time"); "felling foes" unnatural
- m6302#129 | ドモン・カッシュの心がさらに / 燃え上がって行きます。 | Domon Kasshu's warrior spirit blazes / even brighter. | Domon Kasshu's heart burns / ever hotter. | 心 = heart (was "warrior spirit"), same word as #130
- m6302#130 | そして、その心が明鏡止水の境地に / 到達した時― | And when his mind reaches the realm of serene clarity― | And when that heart reaches the / serene state of Meikyo Shisui... | forbidden ― (accepted fix) -> ...; 明鏡止水 = Meikyo Shisui as in #131-133
- m6302#132 | 明鏡止水モードでは、さらに強力な / 必殺技を使用することができます。 | In Meikyo Shisui Mode, you can unleash even more / devastating special finishers. | In Meikyo Shisui Mode, you can use / even more powerful special finishers. | width (ERRO)
- m6302#136 | ミサイルの誘導機能を、 / 一定時間無効化できる機能です。 | This function nullifies missile tracking / for a set period of time. | This function nullifies missile / guidance for a set duration. | same JP term as #134: "missile guidance" (was "tracking")
- m6302#138 | 多数の敵や、強力な武装を持つ敵と / 戦う時などに有効に活用してください。 | Utilize it effectively when fighting large groups / or foes with heavy armaments. | Use it well against many enemies or / enemies with powerful weapons. | width (ERRO)
- m6302#140 | ディストーションフィールドは、 / 重力波を利用したバリアの一種で、 | Distortion Field is a barrier utilizing gravity waves / that deflects energy-based weapons. | The Distortion Field is a barrier / that uses gravity waves, and | width (ERRO); row had invented the content of #141; JP sentence continues (で、)
- m6302#141 | エネルギー系兵器の攻撃を / そらすことができます。 | It turns aside attacks from incoming / energy-type weaponry. | it can turn aside attacks from / energy-type weapons. | continuation of #140 (lowercase), one sentence across rows
- m6302#143 | バルキリー系のユニットは、 / ３段変形のアビリティを持っており、 | Valkyrie-type units possess 3-stage variable ability, / transforming into 3 configurations: | Valkyrie-type units have the 3-Stage / Transformation Ability, and | width (ERRO); 3-Stage Transformation Ability (label #290), sentence continues in #144
- m6302#144 | ファイター形態、ガウォーク形態、 / バトロイド形態の３形態に変形できます。 | Fighter mode, GERWALK mode, / and Battroid mode. | can transform into 3 modes: Fighter, / GERWALK, and Battroid. | rewritten to continue #143 (の３形態に変形できます was lost)
- m6302#145 | 各形態への変形は、昇順変形と / 降順変形で操作することができます。 | Transformation can be controlled via Ascending / and Descending shift commands. | Switch modes with the Ascending and / Descending Transform commands. | width (ERRO)
- m6302#146 | 昇順はバトロイド、ガウォーク、ファイターの / 順に変形し、降順はその逆に変形します。 | Ascending shifts Battroid -> GERWALK -> Fighter, / while Descending reverses the order. | Ascending goes Battroid, GERWALK, / Fighter, and Descending the reverse. | width (ERRO); "->" arrows removed
- m6302#148 | 操作は他の戦闘機形態と同様ですが、 / 飛行中のダッシュターンが可能です。 | Controls match Fighter mode, with the addition / of high-speed Dash Turns in flight. | It controls like other fighter modes, / but can also Dash Turn in flight. | width (ERRO); 他の戦闘機形態と同様 restored, invented "high-speed" removed
- m6302#149 | ガウォーク形態は、ファイター形態と / バトロイド形態の中間に当たる形態です。 | GERWALK mode is the intermediate form between / Fighter and Battroid modes. | GERWALK mode is halfway between / Fighter and Battroid modes. | width (ERRO)
- m6302#151 | バトロイド形態は、人型の通常形態です。 /  | Battroid mode is the humanoid combat form. | Battroid mode is the humanoid / Normal mode. | 人型の通常形態 = humanoid Normal mode (was "combat form")
- m6302#152 | 射撃性能は劣りますが、近接攻撃が可能で、 / 格闘戦に優れます。 | Though ranged output is lower, it possesses melee / attacks and excels in hand-to-hand combat. | Its shooting is weaker, but it can use / Melee and excels at close combat. | width (ERRO)
- m6302#153 | 各形態の特性を把握した上で、 / 戦術に合わせて使い分けましょう。 | Learn each mode's distinct properties and switch / between them according to your tactics. | Learn each mode's traits and switch / between them to suit your tactics. | width (ERRO)
- m6302#155 | まひしたユニットは一定時間動けなくなり、 / 攻撃･防御共に、大きな隙が生じます。 | Paralyzed units are immobilized for a duration, / leaving them wide open to attack. | A paralyzed unit is frozen for a time, / wide open in both attack and defense. | width (ERRO); 攻撃･防御共に restored
- m6302#156 | ガーディアン砲は、衛星「ガーディアン」 / から呼び出す、高出力の支援砲撃です。 | The Guardian Cannon calls down high-output fire support / from the satellite Guardian. | The Guardian Cannon calls high-output / support fire from satellite "Guardian". | width (ERRO); 「ガーディアン」 -> "Guardian"
- m6302#157 | 支援砲撃の出力は、オペレートすることが / 可能です。 | You can calibrate the output of this orbital support / bombardment. | You can control the output of the / support fire. | "orbital ... bombardment" padding; same "support fire" as #156
- m6302#158 | 攻撃ボタンを押し続けることで、 / より高出力の砲撃が発動します。 | Holding the attack button unleashes a significantly / higher-output strike. | Hold the attack button to unleash a / higher-output barrage. | invented "significantly" removed
- m6302#159 | ガーディアン砲の有効範囲は、地球から / 数十万キロメートルの宙域に限られています。 | The effective range of the Guardian Cannon is limited / to within several hundred thousand km of Earth. | Guardian Cannon range is limited to / several hundred thousand km of Earth. | width (ERRO)

### xb_03 (20 fixes)

- m6302#161 | リーンの翼は、ユニットのアーマーが / 一定以下になると自動的に発動します。 | Wings of Rean activate automatically once the unit's / Armor drops below a set threshold. | Wings of Rean auto-activate when / the unit's Armor falls to a set level. | width (ERRO)
- m6302#162 | 発動中は、ユニットの性能が / 大幅に上昇するとともに、 | While active, unit specs increase drastically, / and | While active, the unit's performance / rises greatly, and | bad break ", / and"
- m6302#166 | 展開中には移動することも可能です。 / 強襲を仕掛ける際などに利用しましょう。 | Movement is possible while deployed. Utilize it / when executing assault charges. | You can also move while it's deployed. / Use it when launching an assault. | width (ERRO)
- m6302#167 | 強力な攻撃を受けた時や、特定の攻撃を / 行った時には、強制的に解除されます。 | It is forcibly cancelled upon receiving heavy attacks / or executing specific attacks. | It is forcibly canceled if you take / a strong hit or use certain attacks. | width (ERRO)
- m6302#168 | トランスユニットは、遠隔兵器を利用して / 多方向からの攻撃を行うウェポンです。 | Trans Units are weapons that utilize remote drones / to attack from multiple directions. | The Trans Unit is a Weapon that uses / remote pods to attack from all angles. | width (ERRO)
- m6302#170 | トランスユニットの展開中は、 / ユニットを経由して対象を攻撃します。 | While Trans Units are deployed, attacks strike / the target channeled through the units. | While the Trans Units are deployed, / you attack the target through them. | width (ERRO)
- m6302#171 | ファンネルは、対象を自動追尾して / 攻撃するタイプのウェポンです。 | Funnels are remote weaponry that automatically track / and attack the target. | Funnels are a Weapon type that tracks / and attacks the target automatically. | width (ERRO)
- m6302#172 | 射出するだけで、ロック対象に対して / 自動的に攻撃を開始します。 | Simply launching them will cause them to automatically / attack the locked target. | Just launch them, and they will / attack the locked target automatically. | width (ERRO)
- m6302#173 | 非常に強力な反面、弾数制限があり、 / 敵に破壊される場合もあります。 | While extremely potent, ammunition is limited / and they can be shot down by foes. | They are very powerful, but ammo is / limited and enemies can destroy them. | width (ERRO)
- m6302#175 | アクティブクロークはビーム攻撃の / ダメージを軽減することが可能です。 | Active Cloak allows you to mitigate damage taken / from incoming beam attacks. | Active Cloak can reduce damage / from beam attacks. | width (ERRO)
- m6302#179 | Ｉフィールドは、強力な磁場を発生させ、 / ビーム攻撃を無効化させるバリアです。 | An I-Field is a barrier generating a powerful magnetic / field to nullify beam attacks. | The I-Field is a powerful magnetic / barrier that nullifies beam attacks. | width (ERRO)
- m6302#180 | 非常に強力な反面、持続時間が限られている / ため、適切なタイミングで使用しましょう。 | While extremely powerful, duration is limited, / so deploy it at the appropriate moment. | It is very powerful, but its duration is / limited, so use it at the right time. | width (ERRO)
- m6302#181 | Ｉフィールドは、強力な磁場を発生させ、 / 各種兵器を無効化させるバリアです。 | An I-Field generates a magnetic field barrier / to nullify incoming attacks. | The I-Field is a powerful magnetic / barrier that nullifies various weapons. | 強力な dropped; 各種兵器 = various weapons; parallel with #179
- m6302#183 | 持続時間が限られているとともに、 / 地形に接触すると自動的に解除されます。 | Its duration is limited, and it automatically / deactivates upon contact with terrain. | Its duration is limited, and it ends / automatically on contact with terrain. | width (ERRO)
- m6302#185 | ダミー・バルーンは、ダミーを射出して、 / 敵の照準をかく乱するウェポンです。 | Dummy Balloons are weapons launched to confuse / and scramble enemy targeting. | The Dummy Balloon is a Weapon that / fires decoys to throw off enemy aim. | width (ERRO); ダミーを射出 = fires decoys
- m6302#186 | 射出後から一定時間経つと爆発して、 / 周辺にダメージを与えることもできます。 | After a set duration post-launch, they explode, / inflicting splash damage around them. | A set time after launch, they explode / and can also damage nearby targets. | width (ERRO)
- m6302#188 | ハイパージャマーを起動すると、一定時間 / 敵のロック機能を避けることができます。 | Activating the Hyper Jammer prevents enemy lock-on / for a set period of time. | Activating the Hyper Jammer lets you / evade enemy lock-on for a set time. | width (ERRO)
- m6302#189 | 強力な攻撃を回避したい時などの / 防御手段として活用してください。 | Use it as a defensive measure when you wish / to evade powerful incoming strikes. | Use it as a defense, such as when you / want to avoid a powerful attack. | width (ERRO)
- m6302#197 | ウェポン７：ウイングキャリバー変形 | Weapon 7: Wing Calibur Transform | Weapon 7: Wing Caliber Transform | Wing Caliber (established spelling; was "Calibur")
- m6302#214 | ウェポン４：ウィンゲルバインダー | Weapon 4: Wingel Binder | Weapon 4: Winger Binder | glossary: Winger Binder

### xb_04 (4 fixes)

- m6302#275 | ウェポン２：拡散ビーム・ショット・ライフル | Weapon 2: Scatter Beam Shot Rifle | Weapon 2: Diffuse Beam Shot Rifle | 拡散 = Diffuse, as in #277 (was "Scatter")
- m6302#286 | ウェポン２：有線クローアーム | Weapon 2: Wire Claw Arm | Weapon 2: Wired Claw Arm | glossary: 有線クローアーム = Wired Claw Arm
- m6302#287 | ウェポン３：有線クローアーム（ホールド） | Weapon 3: Wire Claw Arm (Hold) | Weapon 3: Wired Claw Arm (Hold) | glossary: Wired Claw Arm
- m6302#298 | ウェポン４：超高機動マイクロミサイル | Weapon 4: High-Maneuver Micro Missile | Weapon 4: Ultra High-Maneuver / Micro Missile | 超 dropped ("Ultra")

### xd_01 (10 fixes)

- m6340#0 | 敵機体の全撃破 | Destroy All Enemy Units | Destroy all enemy units | objective style of the approved missions (sentence case)
- m6342#0 | 敵機を１００機以上撃破 | Destroy 100 or More Enemy Units | Destroy at least 100 enemy units | objective style (m6042: "Destroy at least 20 enemy units")
- m6342#1 | できるだけ多くの敵機を撃破 | Destroy As Many Enemy Units As Possible | Destroy as many enemies as possible | width (ERRO, 1 line); sentence case
- m6360#0 | エステバリス３機に勝利 | Defeat 3 Aestivalis Units | Defeat 3 Aestivalis | sentence case
- m6900#0 | 貯蔵庫の全破壊 | Destroy All Storage Depots | Destroy all storage depots | sentence case
- m6900#2 | ウィル・ウィプスの撃沈 | Sink the Will Wips | Sink the Will Wipps | glossary: Will Wipps (was "Will Wips", passed only via "Will")
- m6900#22 | これは・・・戦艦ウィル・ウィプスです！ | It is... the battleship Will Wips! | It is... the battleship Will Wipps! | glossary: Will Wipps
- m6900#28 | ウィル・ウィプスの破壊を確認！ | Destruction of the Will Wips confirmed! | Will Wipps destruction confirmed! | glossary: Will Wipps; fits 1 line
- m6900#39 | 敵の逃走を確認！ | Enemy retreat confirmed! | Enemy escape confirmed! | 逃走 = escape (cf. #11 逃走の準備), not 撤退 "retreat" (#29)
- m6900#42 | Ｅ戦区の戦線が崩壊した模様！ | The front line in Sector E has collapsed! | The front line in Sector E appears / to have collapsed! | 模様 = appears to (hedge was turned into fact)
## Doubts left unchanged (for the project owner)

- **m6302#198 フレイボム = "Flame Bomb"**: no official English. Variants: "Frey Bomb" (Bandai Robot Spirits "Frey bomb
  effect"), "Flare Bomb" (akurasu ACE2 database), "Frei Bomb" (fan usage). Kept; choose one for the glossary.
- **m6302#242 ショーター = "Shorter"**: literal katakana; akurasu lists "Shooter" for Nelly/Yuu Brain. Unverified.
- **m6302#249 リムーブドアーム = "Removed Arm"**: literal; akurasu writes "Removable Arm".
- **m6302#246 / #154 スリットウエハー = "Slit Wafer"** (akurasu "Slit Waver"); **#222 "Lasered Buzzsaw"**, **#229/#233
  "Railcannon"** (Dragonar sources write "Rail Cannon"/"Rail Gun"), **#285 "Deflection Mega Particle Cannon"**
  (akurasu "Deflected"), **#303 オーラ斬波 "Aura Slash Wave"**: kept, none of these is in the glossary. A weapon-name
  table for ACE2 does not exist yet; when the command list / unit weapon names are translated, these labels must match it.
- **m6302#219 Ｖ－ＭＵＸＩＭＵＭ発動**: the Japanese has a typo (MUXIMUM); the English "V-MAXIMUM Activate" corrects it. Kept.
- **Label pattern "X Transform" / "V-MAX Activate"** (#197, #206, #213, #217, #219, #220, #307): akurasu uses
  "Wing Caliber Transformation", "Prowler Transformation". Kept the translator's shorter pattern; only the spelling
  Wing Caliber was fixed.
- **m6302#145 昇順変形/降順変形 "Ascending/Descending Transform commands"**: depends on how the command list names these
  inputs (not translated yet).
- **m6302#8, #120, #174 でしょう/ましょう**: polite tutorial softeners rendered as plain statements/imperatives; not a factual hedge.
- **m6900#9-10 "We must destroy all storage depots / by any means necessary."**: "we" is not in the Japanese (passive
  possible), but it is natural for the commander. Kept.
- **m6900#25-27, #50-51** (Drake-side speaker, not identified: Drake, Bishot or the Black Knight): "Here we come,
  Upper Worlders!" assumes a plural "we" for いくぞ. 地上人 = "Upper World(er)" is not in the glossary yet (INDICE lists
  地上人 as a Byston Well term); confirm the rendering used in the op mission tables.
- **m6900#56** "You will surely guide the nation / our father envisioned." (導いてゆけるはずだ = "should be able to
  lead"): slightly stronger than the Japanese; acceptable for Zechs, kept.
- **m6998#0** dev font-test string: translator added "test string" to the kanji list. Never shown to players; kept.
- **m6361 スカル小隊 "Skull Squadron"** and **m6351 ドラグナー１型 "Dragonar-1"**: not in GLOSSARIO; check unit_names/op tables.
- Tutorial rows reused by several units (see list above) were kept generic ("it", "the unit"); the binder/claw rows use
  "the unit" for 機体 instead of "craft".
