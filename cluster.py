class Cluster:
    def __init__(self, cluster):
        self.cluster = cluster['cluster']
        self.auto_scaling_groups = cluster['autoScalingGroups']
        self.uid = self.cluster
