# coding:utf8
import rdflib
import jieba
import re
g = rdflib.Graph()

def create():
    illness=rdflib.URIRef('无先兆偏头痛')
    times = rdflib.Literal(5)
    Times = rdflib.URIRef('次数')
    minLast=rdflib.Literal(4)
    MinLast = rdflib.URIRef('最短持续时间')
    maxLast = rdflib.Literal(72)
    MaxLast = rdflib.URIRef('最长持续时间')
    part = rdflib.URIRef('单侧')
    Part = rdflib.URIRef('部位')
    type = rdflib.URIRef('搏动性')
    Type = rdflib.URIRef('疼痛类型')
    depth = rdflib.URIRef('中重度')
    Depth = rdflib.URIRef('疼痛程度')
    factor = rdflib.URIRef('日常活动')
    Factor = rdflib.URIRef('加重因素')
    action1 = rdflib.URIRef('恶心')
    Action = rdflib.URIRef('伴随症状')
    action2 = rdflib.URIRef('呕吐')
    action3 = rdflib.URIRef('畏光')
    action4 = rdflib.URIRef('畏声')

    g.add((illness, Times, times))
    g.add((illness, MinLast, minLast))
    g.add((illness, MaxLast, maxLast))
    g.add((illness, Part, part))
    g.add((illness, Type, type))
    g.add((illness, Depth, depth))
    g.add((illness, Factor, factor))
    g.add((illness, Action, action1))
    g.add((illness, Action, action2))
    g.add((illness, Action, action3))
    g.add((illness, Action, action4))
    g.serialize('headache.rdf', format='n3')

def query():
    g.parse('headache.rdf', format='n3')

    question=input()


    q="select ?part where { <无先兆偏头痛> <伴随症状> ?part}"
    x = g.query(q)
    t=list(x)
    print(len(t))
    print(t[3][0])

# 定义关键词


# 无先兆偏头痛的伴随症状有哪些？

if __name__ == '__main__':
    create()
    query()
