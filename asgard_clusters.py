import os

import requests

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


def get_clusters_from_cache():
    return alfred_clusters_cache_file.read_json_file()


def create_clusters_cache():
    clusters = get_clusters_from_asgard()
    items = [Item(cluster.cluster, base_url).__dict__ for cluster in clusters]
    items_dict = {'items': items}
    return alfred_clusters_cache_file.write_to_file(items_dict)


if __name__ == '__main__':
    # for debugging the app
    os.environ['alfred_workflow_data'] = '/tmp/asgard'
    # print get_clusters_from_asgard()
    # clusters_cache = create_clusters_cache()
    # print clusters_cache
    print get_clusters_from_cache()
