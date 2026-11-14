import numpy as np
from sklearn.ensemble import RandomForestClassifier
MODEL_VERSION="trustshield-demo-1.0"
def train_demo_model():
 rng=np.random.default_rng(42); n=2400
 amount=rng.lognormal(4.0,1.2,n); ip=rng.uniform(0,100,n); age=rng.exponential(180,n)
 failed=rng.poisson(.7,n); new=rng.binomial(1,.22,n); emulator=rng.binomial(1,.04,n); country=rng.binomial(1,.12,n)
 signal=.025*ip+.65*np.log1p(amount)-.012*age+1.15*failed+1.4*new+2*emulator+1.1*country+rng.normal(0,1.2,n)
 y=(signal>4.1).astype(int); X=np.column_stack([amount,ip,age,failed,new,emulator,country])
 model=RandomForestClassifier(n_estimators=100,max_depth=8,random_state=42,class_weight="balanced")
 model.fit(X,y); return model
MODEL=train_demo_model()
