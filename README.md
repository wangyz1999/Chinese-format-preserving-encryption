# 中文保格式加密
# Chinese-format-preserving-encryption

基于Feistel保格式加密算法，使用THULA中文分词系统，期望能将任意中文句子通过保格式加密的方式将其变为另外的句子，维持其语义结构
Aiming to use Feistel-based encryption (FFX) algorithm and THULA (THU Lexical Analyzer for Chinese) Part of speech tagger to encrypt any Chinese sentence while preserving the semantic sentence structure

## 应用场景
目前保格式加密算法的主要应用是加密数据库信息以保护用户隐私，如姓名、邮箱、银行卡号等。但这些应用场景加密的信息需要严格的格式

本人希望能将任何句子进行加密，其目的主要是好玩

如果不考虑解密功能，纯粹的词性替换同时保存语义结构可以实现句子生成器一类的效果

## 连接

[THULAC：一个高效的中文词法分析工具包] (https://github.com/thunlp/THULAC-Python)
[pyffx](https://github.com/emulbreh/pyffx/)

## 期望效果

原话：我3月27号的下午在北京看见了一只小狗
加密：他6月12号的傍晚与湖南吃掉了两条红鱼
解密：我3月27号的下午在北京看见了一只小狗

原话分词: 我_r 3月_t 27号_t 的_u 下午_t 在_p 北京_ns 看见_v 了_u 一_m 只_q 小_q 狗_n
加密分词: 他_r 6月_t 12号_t 的_u 傍晚_t 与_p 湖南_ns 吃掉_v 了_u 两_m 条_q 红_q 鱼_n

## 解释 
通过分词器对原话进行分词，每个分词片段将有一个对应的词性字典，从中根据Feistel加密找取对应替换词，并以此生成加密句子。解密则需要对加密的话再次进行分词，如分词结构一样则可以百分之百将原话解密。若分词结构不完全一样则只能部分解密，或无法解密。

## 目前版本
在对词性字典库进行了长度分类后，解密的成功率极大提升。下一步提升将对词频进行分类，高频词汇只会加密成高频词汇，防止因低频词导致解密时分词器判断错误的情况


## 词性解释

```
n/名词 np/人名 ns/地名 ni/机构名 nz/其它专名
m/数词 q/量词 mq/数量词 t/时间词 f/方位词 s/处所词
v/动词 a/形容词 d/副词 h/前接成分 k/后接成分 
i/习语 j/简称 r/代词 c/连词 p/介词 u/助词 y/语气助词
e/叹词 o/拟声词 g/语素 w/标点 x/其它 
```

## 初步展示

