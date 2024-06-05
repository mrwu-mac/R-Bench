import os
import json
import argparse
import random
import numpy as np
import copy

def eval_pope(answers, labels, qusetion_ids, error_file):
    pos_num = 0
    print(len(answers), len(labels), len(qusetion_ids))
    pred_list, label_list, error_id = [], [], []
    # print(answers.keys())
    for question_id in qusetion_ids:
        ### process answer
        # print(question_id)
        if question_id not in answers.keys():continue
        text = answers[question_id]

        # Only keep the first sentence
        if text.find('.') != -1:
            text = text.split('.')[0]

        text = text.replace(',', '')
        words = text.split(' ')
        if 'No' in words or 'not' in words or 'no' in words:
            pred_list.append(0)
        else:
            pred_list.append(1)
            

        ### process label
        if labels[question_id] and 'no' in labels[question_id].lower():
            label_list.append(0)
        else:
            label_list.append(1)
            pos_num += 1
        
        ## sta_error
        if pred_list[-1] != label_list[-1]:
            # print(question_id)
            error_id.append(question_id)
    
    # with open(error_file, 'w') as fw:
    #     json.dump(error_id, fw)


    pos = 1
    neg = 0
    yes_ratio = pred_list.count(1) / len(pred_list)

    TP, TN, FP, FN = 0, 0, 0, 0
    assert len(pred_list) == len(label_list)
    for pred, label in zip(pred_list, label_list):
        if pred == pos and label == pos:
            TP += 1
        elif pred == pos and label == neg:
            FP += 1
        elif pred == neg and label == neg:
            TN += 1
        elif pred == neg and label == pos:
            FN += 1

    print('TP\tFP\tTN\tFN\tTotal\t')
    print('{}\t{}\t{}\t{}\t{}'.format(TP, FP, TN, FN, TP + FP + TN + FN))

    precision = float(TP) / float(TP + FP + 0.00001)
    recall = float(TP) / float(TP + FN + 0.00001)
    f1 = 2*precision*recall / (precision + recall + 0.00001)
    acc = (TP + TN) / (TP + TN + FP + FN)
    print('Accuracy: {}'.format(acc))
    print('Precision: {}'.format(precision))
    print('Recall: {}'.format(recall))
    print('F1 score: {}'.format(f1))
    print('Yes ratio: {}'.format(yes_ratio))
    print('%.4f, %.4f, %.4f, %.4f, %.4f' % (acc, precision, recall, f1, yes_ratio))

    print('Total_num:', len(label_list))
    print('pos_num', pos_num, 'neg_num', len(label_list)-pos_num)
    # print(filter_ids)
    return [acc, precision, recall, f1, yes_ratio] 

def eval_box(answers, label_list, qusetion_ids):
    
    # labels = json.load(open(label_file, 'r'))
    # label_list = [q['label'] for q in labels]

    filter_ids = []
    pred_list = []
    pos_num = 0
    for answer, question_id, label in zip(answers, qusetion_ids, label_list):
        text = answer['text']
        if label[0].lower() in text:
            pos_num += 1

    print('Accuracy: {}'.format(pos_num / len(answers)))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--annotation-dir", type=str)
    parser.add_argument("--question-file", type=str)
    parser.add_argument("--question-id-file", type=str)
    parser.add_argument("--result-file", type=str)
    parser.add_argument("--error-file", type=str)
    parser.add_argument("--eval_box", action='store_true', default=False)
    parser.add_argument("--eval_instance", action='store_true', default=False)
    parser.add_argument("--eval_image", action='store_true', default=False)
    parser.add_argument("--eval_obj", action='store_true', default=False)
    parser.add_argument("--eval_web", action='store_true', default=False)
    args = parser.parse_args()

    category = args.question_file.split('/')[-1].split('.')[0]
    print('Category: {}, # samples: {}'.format(category, -1))
    # questions = [json.loads(line) for line in open(args.question_file)]
    if args.eval_box:
        answers = [json.loads(q) for q in open(args.result_file)]
        label_list = [json.loads(q)['label'] for q in open(args.question_file, 'r')]
        eval_box(answers, label_list, answers)
    elif args.eval_web:
        questions = json.load(open(args.question_file, "r"))
        questions = {question['question_id']: question for question in questions}
        labels = json.load(open(args.question_file, 'r'))
        answers = [json.loads(q) for q in open(args.result_file)]
        answers_list = {a['question_id']: a['text'] for a in answers}
            # labels = json.load(open(args.question_file, 'r'))
        label_list = {q['question_id']:q['label'] for q in labels }

        qids_all = questions.keys()
        qids_counterfactual = [q['question_id'] for q in labels if q['type'] == 'counterfactual']
        qids_illusion = [q['question_id'] for q in labels if q['type'] == 'illusion']
        print('counterfactual:', eval_pope(answers_list, label_list, qids_counterfactual, None)[0] * 100)
        print('illusion:', eval_pope(answers_list, label_list, qids_illusion, None)[0] * 100)
        print('total:', eval_pope(answers_list, label_list, qids_all, None)[0] * 100)
    elif args.eval_instance:
        questions = json.load(open(args.question_file, "r"))
        # labels = json.load(open(args.question_file, 'r'))
        labels = questions
        answers = [json.loads(q) for q in open(args.result_file)]
        questions = {question['question_id']: question for question in questions}
        
        resluts = []
        for i in range(1,6): 
            question_ids = json.load(open(args.question_id_file.replace('holder', str(i)) , 'r'))
            print(args.question_id_file.replace('holder', str(i)).split('/')[-1])
            print(len(list(set(question_ids))))
            # id_map = json.load(open('/home/wmr/VLM/Rel_H/dataset/nocaps/local_id_map.json', 'r')) # only for question_v2_local_so_r_out_box/mask
            # answers_list = {id_map[str(a['question_id'])]: a['text'] for a in answers}
            answers_list = {a['question_id']: a['text'] for a in answers}
            # labels = json.load(open(args.question_file, 'r'))
            label_list = {q['question_id']:q['label'] for q in labels }
            result = eval_pope(answers_list, label_list, question_ids, args.error_file)
            resluts.append(result)
        results = np.round(np.mean(np.multiply(np.array(resluts), 100), axis=0), decimals=2)
        print('Average:', results) 
    elif args.eval_image:
        questions = json.load(open(args.question_file, "r"))
        questions = {question['question_id']: question for question in questions}
        labels = json.load(open(args.question_file, 'r'))
        answers = [json.loads(q) for q in open(args.result_file)]

        
        resluts = []
        for i in range(1,6): 
            question_ids = json.load(open(args.question_id_file.replace('holder', str(i)) , 'r'))
            print(args.question_id_file.replace('holder', str(i)).split('/')[-1])
            print(len(list(set(question_ids))))
            answers_list = {a['question_id']: a['text'] for a in answers}
            # labels = json.load(open(args.question_file, 'r'))
            label_list = {q['question_id']:q['label'] for q in labels}
            result = eval_pope(answers_list, label_list, question_ids, args.error_file)
            resluts.append(result)
        results = np.round(np.mean(np.multiply(np.array(resluts), 100), axis=0), decimals=2)
        print('Average:', results)
    elif args.eval_obj:
        questions = json.load(open(args.question_file, "r"))
        questions = {question['question_id']: question for question in questions}
        labels = json.load(open(args.question_file, 'r'))
        answers = [json.loads(q) for q in open(args.result_file)]

        
        resluts = []
        for i in range(1,6): 
            question_ids = json.load(open(args.question_id_file.replace('holder', str(i)) , 'r'))
            print(args.question_id_file.replace('holder', str(i)).split('/')[-1])
            print(len(list(set(question_ids))))
            answers_list = {a['question_id']: a['text'] for a in answers}
            # labels = json.load(open(args.question_file, 'r'))
            label_list = {q['question_id']:q['label'] for q in labels}
            result = eval_pope(answers_list, label_list, question_ids, None)
            resluts.append(result)
        results = np.round(np.mean(np.multiply(np.array(resluts), 100), axis=0), decimals=2)
        print('Average:', results)
    print("====================================")
    
