"""Operation 01 remaining layers for build 0.0.2: tactical briefings 63028/63029, mission 6012, debrief 63168,
Preventer reports 63196/63197. Keyed by row index of the exported table (asserted against the Japanese start).
Names follow work/glossary (checked by tools/ace2/check_names.py after the research merge)."""
import json, sys
sys.path.insert(0, r"D:\Ace 2\tools\ace2")

EN = r"D:\Ace 2\work\translation\en\%s.json"
FILL = r"D:\Ace 2\work\translation\en\_fill\%s.json"
SIG = '\u3000' * 19  # report signature: right-aligned with fullwidth spaces, re-measured by pad_signature()

T = {}
T['brief63028'] = [
 ('ユニットの損傷', "Unit Damage"),
 ('損傷率', "Damage Rate %d％"),
 ('<op(38,1)><sp(2)>さて', "<op(38,1)><sp(2)>Now, let's see what this #c[5E8FD8]new unit#c of yours<im(1)> can do.\n#c[F07141]I'll give detailed orders out there#c,<tr(1)>\nso just sortie for now."),
 ('<op(38,1)><sp(2)>なお', "<op(38,1)><sp(2)>Also, besides you two, the base's rookies\nare holding an exercise elsewhere.\nShow my juniors what you can do, too."),
]
T['brief63029'] = [
 ('ユニットの損傷', "Unit Damage"),
 ('損傷度', "Damage Level %d"),
 ('<op(38,1)><sp(0)>緊急事態', "<op(38,1)><sp(0)>We have an emergency.<im(3)>\nThis base is under attack."),
 ('<op(38,1)><sp(0)>敵は', "<op(38,1)><sp(0)>The enemy seems to be #c[E2E258]Zeon remnants#c, and the\n#c[BE5050]Gundam Unit 2 prototype#c delivered today<tr(1)><im(2)>\nhas been stolen."),
 ('<op(38,1)><sp(0)>#c[BE5050]２号機#cには', "<op(38,1)><sp(0)>I'm told #c[BE5050]Unit 2#c carries a nuclear warhead.<im(7)>\nWe can't let them have it."),
 ('<op(38,1)><sp(0)>#c[BE5050]２号機#cはまだ', "<op(38,1)><sp(0)>#c[BE5050]Unit 2#c is still fighting inside the base.\n#c[F07141]We will stop it#c, no matter what."),
 ('<op(38,1)><sp(0)>ケプフォード', "<op(38,1)><sp(0)>Kepford! Carson!<im(8)>\nSorry, but I need you two out there now."),
 ('<op(38,1)><sp(0)>それとだな', "<op(38,1)><sp(0)>And one more thing...\nEnsign Kou Uraki apparently sortied in\n#c[5E8FD8]Gundam Unit 1#c on his own."),
 ('<op(38,1)><sp(0)>余裕があれば', "<op(38,1)><sp(0)>If you can,<of(1)> back him up as well."),
 ('<op(50,1)><sp(2)>念のため', "<op(50,1)><sp(2)>Let me remind you both, just in case.\nThe final test may be over, but\nthe Gun Ark is not yet complete."),
 ('<op(50,1)><sp(2)>規定レベル', "<op(50,1)><sp(2)>In normal operation within the rated output,\nthere is no problem at all..."),
 ('<op(50,1)><sp(2)>出力を', "<op(50,1)><sp(2)>But if you raise the output to MAX,\nthe energy core becomes unstable."),
 ('<op(50,1)><sp(2)>本来ならば', "<op(50,1)><sp(2)>We meant to readjust it\nbefore your sortie...\nbut in this situation, that's impossible."),
 ('<op(50,1)><sp(2)>応急処置', "<op(50,1)><sp(2)>As a stopgap, I'll put a limiter\non the throttle."),
 ('<op(50,1)><sp(2)>このリミッター', "<op(50,1)><sp(2)>Never remove this limiter.\nThe core could run out of control."),
 ('<op(50,1)><sp(2)>バニング大尉', "<op(50,1)><sp(2)>Lieutenant Burning, please make sure\nthey don't push too hard.\nBoth of you, be careful..."),
]
T['brief63168'] = [
 ('<op(38,1)><sp(2)><im(1)>全員', "<op(38,1)><sp(2)><im(1)>Everyone, stay where you are and listen.\nCommodore #c[E2E258]Kowen#c will brief us\non our operations from here on."),
 ('<op(39,1)><sp(2)>コーウェンだ', "<op(39,1)><sp(2)>This is Kowen. From now on, the #c[5E8FD8]Albion#c<im(2)>\nwill operate under my command.\nI'm counting on you."),
 ('<op(39,1)><sp(2)>まず', "<op(39,1)><sp(2)>First, let me explain what comes next.\nThe #c[5E8FD8]Albion#c will continue<im(4)>\nits pursuit of #c[BE5050]Gundam Unit 2#c."),
 ('<op(39,1)><sp(2)>ウラキ少尉', "<op(39,1)><sp(2)>Ensign Uraki and Lt. JG Kepford, you will\nalso remain with the #c[5E8FD8]Albion#c team\nfor the pursuit."),
 ('<op(39,1)><sp(2)>事態は深刻', "<op(39,1)><sp(2)>The situation is grave.\nThat #c[BE5050]Unit 2#c carries a nuclear warhead\nbanned under the #c[E2E258]Antarctic Treaty#c."),
 ('<op(39,1)><sp(2)>#c[BE5050]ジオンの残党#cが', "<op(39,1)><sp(2)>Why the #c[BE5050]Zeon remnants#c acted now,\nwe still don't know...\nbut we cannot let them keep it."),
 ('<op(39,1)><sp(2)>また', "<op(39,1)><sp(2)>We've also confirmed that the #c[BE5050]Zeon remnants#c\nwere acting with #c[BE5050]Gigano#c. As for #c[BE5050]Gigano#c's aims,\nI'll have #c[5E8FD8]Intelligence#c look into them."),
 ('<op(39,1)><sp(2)>そして', "<op(39,1)><sp(2)>And then there's that unidentified force...\nWe know nothing about them at all,\nneither who they are nor what they want."),
 ('<op(39,1)><sp(2)>これらから', "<op(39,1)><sp(2)>Taking all this together, it's fair to say\nthis is the worst situation imaginable."),
 ('<op(39,1)><sp(2)>やらねば', "<op(39,1)><sp(2)>There's much to be done, but\nrecovering #c[BE5050]Unit 2#c<im(5)> is the top priority.\nI'm counting on you."),
 ('<op(39,1)><sp(2)>なお', "<op(39,1)><sp(2)>I've also received word that the pilot of\n#c[BE5050]Gundam Unit 2#c is #c[BE5050]Zeon#c's ace,\n#c[E2E258]Lt. Commander Anavel Gato#c."),
 ('<op(39,1)><sp(2)>十分に', "<op(39,1)><sp(2)>Stay fully on your guard.\nThat is all from me."),
 ('<op(38,1)><sp(2)>……ケプフォード', "<op(38,1)><sp(2)>...Lt. JG Kepford.\nAbout Ensign Carson..."),
 ('<op(38,1)><sp(2)>残念ながら', "<op(38,1)><sp(2)>I'm sorry. From the state of her unit,\nit's been judged she could not have survived."),
 ('<op(38,1)><sp(2)>彼女は', "<op(38,1)><sp(2)>She's been declared killed in action and\npromoted two ranks... Not that it's\nmuch of a consolation."),
 ('<op(38,1)><sp(2)>ケプフォード、', "<op(38,1)><sp(2)>Kepford, carry out your duty well,\nfor Ensign Carson's sake, too.\nThat's all I can say for now... Dismissed."),
]
T['brief63196'] = [
 ('<sp(0)>「ジオン残党の動向」', '<sp(0)>"Zeon Remnant Activity"\n\n' + SIG + 'Preventer Lady Une'),
 ('<sp(0)><im(1)>先日', "<sp(0)><im(1)>The recent attack on Torrington Base has\nbeen confirmed as the work of a\n#c[BE5050]Zeon remnant#c organization."),
 ('<sp(0)>#c[BE5050]ジオン残党<im(2)>#cは', "<sp(0)>The #c[BE5050]Zeon remnants<im(2)>#c took, from the #c[5E8FD8]UCE#c ship\n#c[5E8FD8]Albion#c<im(8)> at dock, the #c[BE5050]Gundam Unit 2 prototype#c,\nand they are still on the run."),
 ('<sp(0)>なお#c[BE5050]ガンダム試作２号機<im(9)>#cは', "<sp(0)>Note that #c[BE5050]Gundam Unit 2<im(9)>#c is armed\nwith a strategic nuclear weapon banned\nby the Antarctic Treaty."),
 ('<sp(0)>仮に', "<sp(0)>Should this unit's existence become public,\nthe #c[5E8FD8]UCE#c could not escape\npublic criticism."),
 ('<sp(0)>本件には', "<sp(0)>The involvement of the #c[BE5050]Gigano Empire#c<im(3)> has\nalso been confirmed, revealing that the two\nare working together."),
 ('<sp(0)>#c[BE5050]ギガノス#cの目的', "<sp(0)>#c[BE5050]Gigano#c's aims are unknown, but as foes\nof the #c[5E8FD8]UCE#c, their interests are presumed\nto coincide in some way."),
 ('<sp(0)>また今回', "<sp(0)>Given how well planned the attack was,\ninformation on #c[BE5050]Gundam Unit 2#c\nmay have been leaked to outsiders,"),
 ('<sp(0)>#c[5E8FD8]ＵＣＥ#c内部', "<sp(0)>and a collaborator inside the #c[5E8FD8]UCE#c\ncannot be ruled out.\n"),
 ('<sp(0)>諜報機関', "<sp(0)>The intelligence agency #c[E2E258]Preventer#c will\ncontinue to investigate these incidents\nand report as appropriate."),
]
T['brief63197'] = [
 ('<sp(0)>「未確認勢力の調査報告」', '<sp(0)>"Report on the Unidentified Force"\n\n' + SIG + 'Preventer Lady Une'),
 ('<sp(0)><im(1)>トリントン', "<sp(0)><im(1)>No matching data exists for the<im(4)>\n#c[BE5050]unidentified units#c seen in the Torrington\nattack, and their affiliation is unknown."),
 ('<sp(0)>#c[BE5050]ジオン残党#cや', "<sp(0)>They could be new #c[BE5050]Zeon remnant#c or\n#c[BE5050]Gigano#c units, or a force allied with them,\nbut the circumstances make this unlikely."),
 ('<sp(0)>#c[BE5050]ジオン残党#cらとの', "<sp(0)>They did not act together with the #c[BE5050]Zeon\nremnants#c, nor did they make any move\nrelated to the theft of the Gundam."),
 ('<sp(0)>むしろ', "<sp(0)>Rather, they are better seen as a third force\nthat foresaw the #c[BE5050]Zeon remnants#c' moves<im(3)>\nand acted for some purpose of its own."),
 ('<sp(0)>彼らの所属', "<sp(0)>We intend to investigate their affiliation\nand objectives without delay.\n"),
]
T['m6012'] = [
 ('敵勢力の撃破', "Destroy the enemy forces"),
 ('ＧＰ０２の撃破', "Destroy the GP02"),
 ('ザロムＤの撃破', "Destroy the Zarom D"),
 ('<op()><sp(20)>いやぁー', "<op()><sp(20)>Nooo! My Gundam!<ab(700)><ed()>"),
 ('<op()><sp(20)>奴は核弾頭', "<op()><sp(20)>That thing still has the nuclear warhead!<ab(300)>"),
 ('<sp(20)>いいか', "<sp(20)>Listen, you must get it back!<ab(600)><ed()>"),
 ('<op()><sp(20)>シナプス艦長', "<op()><sp(20)>Captain Synapse, please stop Unit 1!<ab(400)>"),
 ('<sp(20)>テストパイロット', "<sp(20)>Test pilot Ensign Uraki is fighting,\ntrying to capture Unit 2!<ab(700)><ed()>"),
 ('<op()><sp(20)>ウラキの奴', "<op()><sp(20)>Damn that Uraki!<ab(300)><ed()>"),
 ('<op()><sp(20)>ウラキ少尉！', "<op()><sp(20)>Ensign Uraki! This is Synapse of the Albion.<ab(500)>"),
 ('<sp(20)>２号機の奪還', "<sp(20)>Leave recovering Unit 2 to the other\npilots and come back at once!<ab(300)><ed()>"),
 ('<op()><sp(20)>無理です', "<op()><sp(20)>I can't! I'm engaging the enemy! Besides,\nthis fight isn't decided yet!<ab(200)>"),
 ('<sp(20)>やります', "<sp(20)>I'll do it!<ab(500)><ed()>"),
 ('<op()><sp(20)>ふ、意気込み', "<op()><sp(20)>Heh, I admire your spirit.<ab(400)>"),
 ('<sp(20)>だが相手', "<sp(20)>But you are only a fledgling!<ab(700)><ed()>"),
 ('<op()><sp(20)>レーダー', "<op()><sp(20)>Radar contact! Enemy reinforcements!<ab(400)>"),
 ('<sp(20)>この反応', "<sp(20)>This signature... Metal Armors?!<ab(200)>"),
 ('<sp(20)>ギガノスです', "<sp(20)>It's Gigano!<ab(200)><ed()>"),
 ('<op()><sp(20)>馬鹿な', "<op()><sp(20)>Impossible! Check again!<ab(100)><ed()>"),
 ('<op()><sp(20)>間違いありません', "<op()><sp(20)>There's no mistake!<ab(200)><ed()>"),
 ('<op()><sp(20)>さあ、久しぶり', "<op()><sp(20)>Well, it's been a while since our last big job!<ab(300)>"),
 ('<sp(20)>派手に', "<sp(20)>Go out there and raise hell!<ab(200)><ed()>"),
 ('<op()><sp(20)>おう', "<op()><sp(20)>Yeah!<ab(500)><ed()>"),
 ('<op()><sp(20)>ギガノスのメタルアーマー', "<op()><sp(20)>Gigano Metal Armors...<ab(200)>"),
 ('<sp(20)>なぜこんな', "<sp(20)>What are they doing here?<ab(300)><ed()>"),
 ('<op()><sp(20)>タック…気をつけて', "<op()><sp(20)>Tack... be careful!<ab(700)><ed()>"),
 ('<op()><sp(20)>どんな者が', "<op()><sp(20)>Whoever comes, they can't beat us!<ab(100)><ed()>"),
 ('<op()><sp(20)>新たな敵の反応', "<op()><sp(20)>New enemy signatures!<ab(100)><ed()>"),
 ('<op()><sp(20)>き、基地内', "<op()><sp(20)>Th-the base's mobile suits are nearly all gone!<ab(100)><ed()>"),
 ('<op()><sp(20)>周辺に敵機', "<op()><sp(20)>Enemies all around! We can't hold them!<ab(100)><ed()>"),
 ('<op()><sp(20)>被弾箇所', "<op()><sp(20)>Put out the fires where we were hit!<ab(100)><ed()>"),
 ('<op()><sp(20)>ミノフスキー', "<op()><sp(20)>Minovsky particles being dispersed!<ab(100)><ed()>"),
 ('<op()><sp(20)>各部', "<op()><sp(20)>All sections, report damage!<ab(100)><ed()>"),
 ('<op()><sp(20)>目標は無事', "<op()><sp(20)>Looks like the target's secured.<ab(200)>"),
 ('<sp(20)>よし、引き上げる', "<sp(20)>All right, we're pulling out!!<ab(100)><ed()>"),
 ('<op()><sp(20)>撤退命令', "<op()><sp(20)>Retreat order! Hurry!<ab(300)><ed()>"),
 ('<op()><sp(20)>…ギガノスは', "<op()><sp(20)>...Is Gigano covering for Zeon?<ab(600)><ed()>"),
 ('<op()><sp(20)>高熱源体', "<op()><sp(20)>Multiple high heat sources approaching!<ab(200)><ed()>"),
 ('<op()><sp(20)>またギガノス', "<op()><sp(20)>Gigano again?!<ab(200)><ed()>"),
 ('<op()><sp(20)>いえ', "<op()><sp(20)>No... units we've never seen before.<ab(500)><ed()>"),
 ('<op()><sp(20)>なんだこいつら', "<op()><sp(20)>What are these things...?!<ab(500)><ed()>"),
 ('<sp(20)>見たこともない', "<sp(20)>I've never seen units like these...!<ab(500)><ed()>"),
 ('<op()><sp(20)>タック、今は', "<op()><sp(20)>Tack, just focus on intercepting them!<ab(700)><ed()>"),
 ('<op()><sp(20)>偶然にしては', "<op()><sp(20)>Too convenient to be a coincidence.<ab(300)>"),
 ('<sp(20)>こいつらも', "<sp(20)>Are they working together too?<ab(700)><ed()>"),
 ('<op()><sp(20)>あるいは', "<op()><sp(20)>Or perhaps a third force taking\nadvantage of the chaos...<ab(700)><ed()>"),
 ('<op()><sp(20)>な、何なんだ', "<op()><sp(20)>Wh-what is this thing?!<ab(300)>"),
 ('<sp(20)>い、今までの', "<sp(20)>I-it's not like the others!<ab(300)><ed()>"),
 ('<op()><sp(20)>敵機、本艦', "<op()><sp(20)>Enemy unit closing fast on the ship!<ab(50)><ed()>"),
 ('<op()><sp(20)>うああっ', "<op()><sp(20)>Aaagh!<ab(100)><ed()>"),
 ('<op()><sp(20)>大尉', "<op()><sp(20)>Lieutenant?! Are you all right?!<ab(50)><ed()>"),
 ('<op()><sp(20)>バニング大尉が', "<op()><sp(20)>Lt. Burning is wounded! Medic!<ab(100)><ed()>"),
 ('<op()><sp(20)>だ、大丈夫', "<op()><sp(20)>I-I'm fine! Never mind me!<ab(400)><ed()>"),
 ('<op()><sp(20)>このままじゃ', "<op()><sp(20)>At this rate, we're done for...!<ab(600)><ed()>"),
 ('<op()><sp(20)>エネルギーコアからの', "<op()><sp(20)>Something's wrong with the power\nfrom the energy core!<ab(700)>"),
 ('<sp(20)>機体に負担', "<sp(20)>You've pushed the unit too hard!<ab(100)>"),
 ('<sp(20)>サブユニット', "<sp(20)>Start the sub-unit in emergency mode!<ab(200)><ed()>"),
 ('<op()><sp(20)>とっくに', "<op()><sp(20)>Already tried! It's no use!<ab(200)><ed()>"),
 ('<op()><sp(20)>危険だ', "<op()><sp(20)>It's dangerous! Come back right now!<ab(200)><ed()>"),
 ('<op()><sp(20)>ここで退けるか', "<op()><sp(20)>I can't back down now!!<ab(500)><ed()>"),
 ('<op()><sp(20)>タック……今助ける', "<op()><sp(20)>Tack... I'm coming to help!<ab(900)><ed()>"),
 ('<op()><sp(20)>カーソン少尉', "<op()><sp(20)>Ensign Carson! Did you remove the limiter?!<ab(500)>"),
 ('<sp(20)>やめなさい', "<sp(20)>Stop it!<ab(50)>"),
 ('<sp(20)>すぐにスロットル', "<sp(20)>Pull the throttle back right now!!<ab(400)><ed()>"),
 ('<op()><sp(20)>違うタイプ', "<op()><sp(20)>A different type... be careful.<ab(500)><ed()>"),
 ('<op()><sp(20)>私がやらなくては', "<op()><sp(20)>I have to do this...<ab(300)><ed()>"),
 ('<op()><sp(20)>新たな敵影', "<op()><sp(20)>New enemy contact!<ab(300)><ed()>"),
 ('<on()><sp(20)>ここから出す', "<on()><sp(20)>I won't let you get out of here!<ab(0)><off()>"),
 ('<on()><sp(20)>ふん、こしゃく', "<on()><sp(20)>Hmph, how impudent...\nYou! Stay out of my way!<ab(0)><off()>"),
 ('<on()><sp(20)>ああっ', "<on()><sp(20)>Aah...!!<ab(0)><off()>"),
 ('<on()><sp(20)>うああっ', "<on()><sp(20)>Uwaah...!!<ab(0)><off()>"),
 ('<on()><sp(20)>ウラキ少尉！', "<on()><sp(20)>Ensign Uraki! You are still too green\nto make an enemy of me!<ab(0)><off()>"),
 ('<on()><sp(20)>未熟だとぉ', "<on()><sp(20)>Too green?!<ab(0)><off()>"),
 ('<on()><sp(20)>うっ', "<on()><sp(20)>Ngh...!!<ab(0)><off()>"),
 ('<on()><sp(20)>エネルギーコアが臨界', "<on()><sp(20)>The energy core has gone critical...!\nMarina! Stop!<ab(0)><off()>"),
 ('<on()><sp(20)>マリナ！', "<on()><sp(20)>Marina! Don't! Come back!<ab(0)><off()>"),
 ('<on()><sp(20)>タック、ごめん', "<on()><sp(20)>Tack, I'm sorry...<ab(0)><off()>"),
 ('<on()><sp(20)>脱出だ', "<on()><sp(20)>Eject! Eject!<ab(0)><off()>"),
 ('<on()><sp(20)>…さよなら', "<on()><sp(20)>...Goodbye.<ab(0)><off()>"),
 ('<on()><sp(20)>マリナーー', "<on()><sp(20)>MARINAAAAA!!!!!!<ab(0)><off()>"),
]


def pad_signature(jp, en, fm):
    """Right-align the report signature line like the Japanese one (same end position, fullwidth-space indent)."""
    from merge_fill import widths
    jline, eline = jp.split('\n')[-1], en.split('\n')[-1]
    target = widths(fm, jline)[0]
    name = eline.lstrip('　')
    space = widths(fm, '　')[0]
    n = max(0, round((target - widths(fm, name)[0]) / space))
    return en[:len(en) - len(eline)] + '　' * n + name


def main():
    from merge_fill import load_fonts
    menu = load_fonts()['menu']
    for table, pairs in T.items():
        rows = json.load(open(EN % table, encoding='utf-8'))['rows']
        assert len(rows) == len(pairs), (table, len(rows), len(pairs))
        fill = {}
        for i, (row, (start, en)) in enumerate(zip(rows, pairs)):
            assert row['jp'].startswith(start), (table, i, row['jp'][:30], start)
            fill[str(i)] = pad_signature(row['jp'], en, menu) if SIG in en else en
        json.dump(fill, open(FILL % table, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(table, len(fill), 'rows')


if __name__ == '__main__':
    main()
