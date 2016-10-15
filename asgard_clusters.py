import os

import requests
import logging
import json

from alfred_file import AlfredFile, get_workflow_data_dir
from alfred_item import Item
from cluster import Cluster

base_url = "http://asgard.dev-charter.net:8080/us-west-2"

alfred_clusters_cache_file = AlfredFile(get_workflow_data_dir(), "clusters.json")


def get_clusters_from_asgard():
    response = requests.get('{0}/cluster/list.json'.format(base_url))
    if response.ok:
        clusters_json = response.json()
        clusters = [Cluster(cluster_dict) for cluster_dict in clusters_json if cluster_dict[u'cluster']]
        return clusters
    else:
        raise LookupError()


def execute(query):
    """Execute the desired command

    Keyword arguments:
    query   -- The query entered by the user

    """
    clusters_cache = get_clusters_from_cache()
    words = query.split()
    if len(words) == 0:
        print clusters_cache
    else:
        word = words[0]
        stash_cache_dict = json.loads(clusters_cache)
        matches = [x for x in stash_cache_dict['items'] if fulfills_some_condition(x, word)]
        items_dict = {'items': matches}
        items_json = json.dumps(items_dict, sort_keys=True, indent=4, separators=(',', ': '))
        print items_json


def fulfills_some_condition(item, word):
    found = word in item['subTitle']
    return found


def get_clusters_from_cache():
    return alfred_clusters_cache_file.read_json_file()


def create_clusters_cache():
    try:
        clusters = get_clusters_from_asgard()
        items = [Item(cluster.cluster, base_url).__dict__ for cluster in clusters]
        items_dict = {'items': items}
        alfred_clusters_cache_file.write_to_file(items_dict)
        return "Asgard Cluster Cache created successfully."
    except Exception as e:
        logging.error(e)
        return "Failed"


if __name__ == '__main__':
    # for debugging the app
    os.environ['alfred_workflow_data'] = '/tmp/asgard'
    # print get_clusters_from_asgard()
    # clusters_cache = create_clusters_cache()
    # print clusters_cache
    print get_clusters_from_cache()
