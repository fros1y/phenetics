import funcy as f

tier1 = [
    "AnalysisAndModeling",
    "AnatomicalTarget",
    "CognitiveComputingAndLearningSystems",
    "DataAcquisition",
    "DNAMapping/GeneticEngineering",  # Too few examples
    "Imaging",
    "Manufacturing",
    "PersonalizedProduct",  # Everything tagged here
    "SpecificationofUse",
    "SurgicalMethod",
    "SurgicalRobotics",
    "SurgicalTracking",
    "Validation",
    "Verification"
]

tier2 = """AnalysisAndModeling_3DModeling
AnalysisAndModeling_Simulation
AnatomicalTarget_LowerExtremity
AnatomicalTarget_Skull
AnatomicalTarget_Torso
AnatomicalTarget_UpperExtremity
DataAcquisition_Diagnostics
DataAcquisition_Genomics
DataAcquisition_InformationDatabase
DataAcquisition_MedicalHistory
Imaging_CT
Imaging_MRI
Imaging_PET
Imaging_SPECT
Imaging_Ultrasound
Imaging_Xray
Manufacturing_AdditiveManufacturing
PersonalizedProduct_AnimalUse
PersonalizedProduct_CustomMaterialProperties
PersonalizedProduct_Guide/Jig
PersonalizedProduct_Implant
PersonalizedProduct_MEMs
PersonalizedProduct_SurgicalInstrument
PersonalizedProduct_WirelessCommunication
SpecificationofUse_Cosmetic
SpecificationofUse_Disease
SpecificationofUse_Fracture
SpecificationofUse_JointReplacement
SpecificationofUse_Trauma
Verification_ImplantFit
Verification_InstrumentDesign""".split("\n")

tier3 = """AnalysisAndModeling_Simulation_FiniteElementAnalysis
AnalysisAndModeling_Simulation_WholeBodyMotionSimulation
AnatomicalTarget_LowerExtremity_Ankle
AnatomicalTarget_LowerExtremity_Hip
AnatomicalTarget_LowerExtremity_Knee
AnatomicalTarget_LowerExtremity_Toes
AnatomicalTarget_Skull_Cranium
AnatomicalTarget_Skull_Jaw
AnatomicalTarget_Torso_Pelvis
AnatomicalTarget_Torso_Spine
AnatomicalTarget_UpperExtremity_Elbow
AnatomicalTarget_UpperExtremity_Fingers
AnatomicalTarget_UpperExtremity_Shoulder
AnatomicalTarget_UpperExtremity_Wrist
DataAcquisition_InformationDatabase_SimilarProfileComparison
PersonalizedProduct_Implant_Drug-elutingImplant
PersonalizedProduct_Implant_StemCellEngineering
PersonalizedProduct_SurgicalInstrument_Patient-specific
PersonalizedProduct_SurgicalInstrument_Surgeon-specific
PersonalizedProduct_WirelessCommunication_IOTenabled
SpecificationofUse_Disease_BoneDisease
SpecificationofUse_Trauma_Military""".split("\n")

tier4 = ["AnatomicalTarget_Skull_Jaw_TMJ"]

all_tiers = tier1 + tier2 + tier3 + tier4

all_tiers_100 = ['AnalysisAndModeling',
 'AnalysisAndModeling_3DModeling',
 'AnatomicalTarget',
 'AnatomicalTarget_LowerExtremity',
 'AnatomicalTarget_LowerExtremity_Hip',
 'AnatomicalTarget_LowerExtremity_Knee',
 'AnatomicalTarget_Torso',
 'AnatomicalTarget_Torso_Spine',
 'AnatomicalTarget_UpperExtremity',
 'AnatomicalTarget_UpperExtremity_Shoulder',
 'Imaging',
 'Imaging_CT',
 'Imaging_MRI',
 'Imaging_Ultrasound',
 'Manufacturing',
 'Manufacturing_AdditiveManufacturing',
 #'PersonalizedProduct',  # All have this
 'PersonalizedProduct_Guide/Jig',
 'PersonalizedProduct_Implant',
 'SpecificationofUse',
 'SpecificationofUse_Disease',
 'SpecificationofUse_JointReplacement',
 'SurgicalMethod']


tier_translations = dict([('AnalysisAndModeling', 'Analysis and Modeling'),
 ('AnalysisAndModeling_3DModeling', 'Analysis and Modeling: 3D Modeling'),
 ('AnatomicalTarget', 'Anatomical Target'),
 ('AnatomicalTarget_Torso_Spine', 'Anatomical Target: Torso - Spine'),
 ('AnatomicalTarget_LowerExtremity', 'Anatomical Target: Lower Extremity'),
 ('AnatomicalTarget_LowerExtremity_Hip',
  'Anatomical Target: Lower Extremity - Hip'),
 ('AnatomicalTarget_LowerExtremity_Knee',
  'Anatomical Target: Lower Extremity - Knee'),
 ('AnatomicalTarget_Torso', 'Anatomical Target: Torso'),
 ('AnatomicalTarget_UpperExtremity', 'Anatomical Target: Upper Extremity'),
 ('AnatomicalTarget_UpperExtremity_Shoulder', 'Anatomical Target: Upper Extremity - Shoulder'),
 ('Imaging', 'Imaging'),
 ('Imaging_CT', 'Imaging: CT'),
 ('Imaging_MRI', 'Imaging: MRI'),
 ('Imaging_Ultrasound', 'Imaging: Ultrasound'),
 ('Manufacturing', 'Manufacturing'),
 ('Manufacturing_AdditiveManufacturing',
  'Manufacturing: Additive Manufacturing'),
 ('PersonalizedProduct', 'Personalized Product'),
 ('PersonalizedProduct_Guide/Jig', 'Personalized Product: Guide or Jig'),
 ('PersonalizedProduct_Implant', 'Personalized Product: Implant'),
 ('SpecificationofUse', 'Specification of Use'),
 ('SpecificationofUse_Disease', 'Specification of Use: Disease'),
 ('SpecificationofUse_JointReplacement',
  'Specification of Use: Joint Replacement'),
 ('SurgicalMethod', 'Surgical Method')])




def array_labels(row, tiers=all_tiers,):
    labels = []
    for c in tiers:
        if c in row and row[c]:
            if c in tier_translations:
                labels.append(tier_translations[c])
    return list(sorted(set(labels)))

def array_labels_textual(row, tiers=all_tiers,):
    labels = []
    for c in tiers:
        if c in row and row[c]:
            if c in tier_translations:
                labels.append(tier_translations[c])
    return ", ".join(sorted(set(labels)))

@f.collecting
def cpc_split(cpcs):
    for code in cpcs:
        yield code
        split_code = code.split('/')
        if split_code:
            yield split_code[0]


def iden(x):
    return x

stopwords = list(set("""able
above-mentioned
accordingly
across
along
already
alternatively
always
among
and/or
anything
anywhere
better
disclosure
due
easily
easy
eg
either
elsewhere
enough
especially
essentially
et al
etc
eventually
excellent
finally
furthermore
good
hence
he/she
him/her
his/her
ie
ii
iii
instead
later
like
little
many
may
meanwhile
might
moreover
much
must
never
often
others
otherwise
overall
rather
remarkably
significantly
simply
sometimes
specifically
straight forward
substantially
thereafter
therebetween
therefor
therefrom
therein
thereinto
thereon
therethrough
therewith
together
toward
towards
typical
typically
upon
via
vice versa
whatever
whereas
whereat
wherever
whether
whose
within
without
yet
i
me
my
myself
we
our
ours
ourselves
you
you're
you've
you'll
you'd
your
yours
yourself
yourselves
he
him
his
himself
she
she's
her
hers
herself
it
it's
its
itself
they
them
their
theirs
themselves
what
which
who
whom
this
that
that'll
these
those
am
is
are
was
were
be
been
being
have
has
had
having
do
does
did
doing
a
an
the
and
but
if
or
because
as
until
while
of
at
by
for
with
about
against
between
into
through
during
before
after
above
below
to
from
up
down
in
out
on
off
over
under
again
further
then
once
here
there
when
where
why
how
all
any
both
each
few
more
most
other
some
such
no
nor
not
only
own
same
so
than
too
very
s
t
can
will
just
don
don't
should
should've
now
d
ll
m
o
re
ve
y
ain
aren
aren't
couldn
couldn't
didn
didn't
doesn
doesn't
hadn
hadn't
hasn
hasn't
haven
haven't
isn
isn't
ma
mightn
mightn't
mustn
mustn't
needn
needn't
shan
shan't
shouldn
shouldn't
wasn
wasn't
weren
weren't
won
won't
wouldn
wouldn't
a
accordance
according
all
also
an
and
another
are
as
at
be
because
been
being
by
claim
comprises
corresponding
could
described
desired
do
does
each
embodiment
fig
figs
for
from
further
generally
had
has
have
having
herein
however
if
in
into
invention
is
it
its
means
not
now
of
on
onto
or
other
particularly
preferably
preferred
present
provide
provided
provides
relatively
respectively
said
should
since
some
such
suitable
than
that
the
their
then
there
thereby
therefore
thereof
thereto
these
they
this
those
thus
to
use
various
was
were
what
when
where
whereby
wherein
which
while
who
will
with
would
able
above-mentioned
already
always
and/or
anything
anywhere
better
disclosure
easily
eg
either
elsewhere
enough
especially
et al
etc
eventually
finally
furthermore
he/she
hence
him/her
his/her
instead
may
meanwhile
might
moreover
must
often
one
one another
otherwise
possibly
rather
remarkably
significantly
simply
sometimes
straight forward
substantially
therebetween
therefor
therefrom
therein
thereinto
thereon
therethrough
therewith
towards
typical
via
vice versa
whatever
whereat
wherever
whether
whose
within
without
wrt
yet""".split("\n")))

import fse
import numpy as np
from gensim.parsing.preprocessing import strip_non_alphanum, strip_punctuation
import sklearn

class Embedder(sklearn.base.BaseEstimator):
    def __init__(self, model):
        self.model = model
        
    def fit(self, sentences, *arg, **kwargs):
        self.model.train(fse.SplitIndexedList(sentences.values))
        return self
    
    def transform(self, sentences):
        return self.model.infer(fse.SplitIndexedList(sentences.values))
        

class Extract(sklearn.base.BaseEstimator):
    def fit(self, *arg, **kwargs):
        return self
    
    def transform(self, vals):
        return np.array([v if v else np.zeros(64) for v in vals])

def citations_split(cites):
    if cites is None:
        return []
    return [strip_non_alphanum(strip_punctuation(c)).replace(' ', '') for c in cites]

