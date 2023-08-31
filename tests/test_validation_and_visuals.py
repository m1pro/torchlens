# This is for validating all the different model types. Have it both validate and spit out the visual for checking.
# Let the default input size be 3x3x224x224.

from os.path import join as opj
import pytest
import torch
import torchvision
import example_models

import cornet
from torchlens import log_forward_pass, show_model_graph, validate_saved_activations

# Define inputs
torch.manual_seed(0)
torch.cuda.manual_seed_all(0)


@pytest.fixture
def default_input1():
    return torch.rand(6, 3, 224, 224)


@pytest.fixture
def default_input2():
    return torch.rand(6, 3, 224, 224)


@pytest.fixture
def default_input3():
    return torch.rand(6, 3, 224, 224)


@pytest.fixture
def default_input4():
    return torch.rand(6, 3, 224, 224)


@pytest.fixture
def zeros_input():
    return torch.zeros(6, 3, 224, 224)


@pytest.fixture
def ones_input():
    return torch.ones(6, 3, 224, 224)


@pytest.fixture
def vector_input():
    return torch.rand(5)


@pytest.fixture
def input_2d():
    return torch.rand(5, 5)


# Test different operations

def test_model_simple_ff(default_input1):
    model = example_models.SimpleFF()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'simple_ff'))


def test_model_inplace_funcs(default_input1):
    model = example_models.InPlaceFuncs()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'inplace_funcs'))


def test_model_simple_internally_generated(default_input1):
    model = example_models.SimpleInternallyGenerated()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'simple_internally_generated'))


def test_model_new_tensor_inside(default_input1):
    model = example_models.NewTensorInside()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'new_tensor_inside'))


def test_model_new_tensor_from_numpy(default_input1):
    model = example_models.TensorFromNumpy()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'new_tensor_from_numpy'))


def test_model_simple_random(default_input1):
    model = example_models.SimpleRandom()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'simple_random'))


def test_dropout_model_real_train(default_input1):
    model = example_models.DropoutModelReal()
    model.train()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'dropout_real_train'))


def test_dropout_model_real_eval(default_input1):
    model = example_models.DropoutModelReal()
    model.eval()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'dropout_real_eval'))


def test_dropout_model_dummy_zero_train(default_input1):
    model = example_models.DropoutModelDummyZero()
    model.train()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'dropout_dummyzero_train'))


def test_dropout_model_dummy_zero_eval(default_input1):
    model = example_models.DropoutModelDummyZero()
    model.eval()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'dropout_dummyzero_eval'))


def test_batchnorm_train(default_input1):
    model = example_models.BatchNormModel()
    model.train()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_buffer_layers=True,
                     vis_outpath=opj('visualization_outputs', 'batchnorm_train_showbuffer'))
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_buffer_layers=False,
                     vis_outpath=opj('visualization_outputs', 'batchnorm_train_invisbuffer'))


def test_batchnorm_eval(default_input1):
    model = example_models.BatchNormModel()
    model.eval()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'batchnorm_eval'))


def test_concat_tensors(default_input1):
    model = example_models.ConcatTensors()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'concat_tensors'))


def test_split_tensor(default_input1):
    model = example_models.SplitTensor()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'split_tensors'))


def test_identity_model(default_input1):
    model = example_models.IdentityModule()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'identity_model'))


def test_assign_tensor(default_input1):
    model = example_models.AssignTensor()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'assigntensor'))


def test_get_and_set_item(default_input1):
    model = example_models.GetAndSetItem()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'get_set_item'))


def test_getitem_tracking(input_2d):
    model = example_models.GetItemTracking()
    assert validate_saved_activations(model, input_2d)
    show_model_graph(model,
                     input_2d,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'getitem_tracking'))


def test_inplace_zero_tensor(default_input1):
    model = example_models.InPlaceZeroTensor()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'inplace_zerotensor'))


def test_slice_operations(default_input1):
    model = example_models.SliceOperations()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'slice_operations'))


def test_dummy_operations(default_input1):
    model = example_models.DummyOperations()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'dummy_operations'))


def test_sametensor_arg(default_input1):
    model = example_models.SameTensorArg()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model,
                     default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'same_tensor_arg'))


def test_multiple_inputs_arg(default_input1, default_input2, default_input3):
    model = example_models.MultiInputs()
    assert validate_saved_activations(model, [default_input1, default_input2, default_input3])
    show_model_graph(model,
                     [default_input1, default_input2, default_input3],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'multiple_inputs_arg'))


def test_multiple_inputs_kwarg(default_input1, default_input2, default_input3):
    model = example_models.MultiInputs()
    assert validate_saved_activations(model, [], {'x': default_input1, 'y': default_input2, 'z': default_input3})
    show_model_graph(model,
                     [],
                     {'x': default_input1, 'y': default_input2, 'z': default_input3},
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'multiple_inputs_kwarg'))


def test_multiple_inputs_arg_kwarg_mix(default_input1, default_input2, default_input3):
    model = example_models.MultiInputs()
    assert validate_saved_activations(model, [default_input1], {'y': default_input2, 'z': default_input3})
    show_model_graph(model,
                     [],
                     {'x': default_input1, 'y': default_input2, 'z': default_input3},
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'multiple_inputs_arg_kwarg_mix'))


def test_list_input(default_input1, default_input2, default_input3):
    model = example_models.ListInput()
    assert validate_saved_activations(model, [[default_input1, default_input2, default_input3]])
    show_model_graph(model,
                     [[default_input1, default_input2, default_input3]],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'list_inputs'))


def test_dict_input(default_input1, default_input2, default_input3):
    model = example_models.DictInput()
    assert validate_saved_activations(model, [{'x': default_input1, 'y': default_input2, 'z': default_input3}])
    show_model_graph(model,
                     [{'x': default_input1, 'y': default_input2, 'z': default_input3}],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'dict_inputs'))


def test_nested_input(default_input1, default_input2, default_input3, default_input4):
    model = example_models.NestedInput()
    assert validate_saved_activations(model, [{'list1': [default_input1, default_input2],
                                               'list2': [default_input3, default_input4]}])
    show_model_graph(model,
                     [{'list1': [default_input1, default_input2],
                       'list2': [default_input3, default_input4]}],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'nested_inputs'))


def test_multi_outputs(default_input1):
    model = example_models.MultiOutputs()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'multi_outputs'))


def test_list_output(default_input1):
    model = example_models.ListOutput()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'list_output'))


def test_dict_output(default_input1):
    model = example_models.DictOutput()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'dict_output'))


def test_nested_output(default_input1):
    model = example_models.NestedOutput()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'nested_output'))


def test_buffer_model():
    model = example_models.BufferModel()
    model_input = torch.rand(12, 12)
    assert validate_saved_activations(model, model_input)
    show_model_graph(model, model_input,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'buffer_model_visible'),
                     vis_buffer_layers=True)
    show_model_graph(model, model_input,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'buffer_model_invisible'),
                     vis_buffer_layers=False)


def test_simple_branching(default_input1):
    model = example_models.SimpleBranching()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'simple_branching_model'))


def test_conditional_branching(zeros_input, ones_input):
    model = example_models.ConditionalBranching()
    assert validate_saved_activations(model, -ones_input)
    assert validate_saved_activations(model, ones_input)
    show_model_graph(model, -ones_input,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'conditional_branching_model_negative'))
    show_model_graph(model, ones_input,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'conditional_branching_model_positive'))


def test_repeated_module(default_input1):
    model = example_models.RepeatedModule()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'repeated_module_model'))


def test_nested_modules(default_input1):
    model = example_models.NestedModules()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'nested_modules_model_fulldepth'))
    show_model_graph(model, default_input1,
                     vis_nesting_depth=1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'nested_modules_model_depth1'))
    show_model_graph(model, default_input1,
                     vis_nesting_depth=2,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'nested_modules_model_depth2'))
    show_model_graph(model, default_input1,
                     vis_nesting_depth=3,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'nested_modules_model_depth3'))
    show_model_graph(model, default_input1,
                     vis_nesting_depth=4,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'nested_modules_model_depth4'))


def test_orphan_tensors(default_input1):
    model = example_models.OrphanTensors()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'orphan_tensors_model'))


def test_simple_loop_no_param(default_input1):
    model = example_models.SimpleLoopNoParam()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'simple_loop_no_param_unrolled'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'simple_loop_no_param_rolled'))


def test_same_op_repeat(vector_input):
    model = example_models.SameOpRepeat()
    assert validate_saved_activations(model, vector_input)
    show_model_graph(model, vector_input,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'same_op_repeat_unrolled'))
    show_model_graph(model, vector_input,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'same_op_repeat_rolled'))


def test_repeated_op_type_in_loop(default_input1):
    model = example_models.RepeatedOpTypeInLoop()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'same_op_type_in_loop_unrolled'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'same_op_type_in_loop_rolled'))


def test_varying_loop_noparam1(default_input1):
    model = example_models.VaryingLoopNoParam1()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'varying_loop_noparam1_unrolled'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'varying_loop_noparam1_rolled'))


def test_varying_loop_noparam2(default_input1):
    model = example_models.VaryingLoopNoParam2()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'varying_loop_noparam2_unrolled'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'varying_loop_noparam2_rolled'))


def test_varying_loop_withparam(vector_input):
    model = example_models.VaryingLoopWithParam()
    assert validate_saved_activations(model, vector_input)
    show_model_graph(model, vector_input,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'varying_loop_withparam_unrolled'))
    show_model_graph(model, vector_input,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'varying_loop_withparam_rolled'))


def test_looping_internal_funcs(default_input1):
    model = example_models.LoopingInternalFuncs()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'looping_internal_funcs_unrolled'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'looping_internal_funcs_rolled'))


def test_looping_from_inputs1(default_input1, default_input2, default_input3):
    model = example_models.LoopingFromInputs1()
    assert validate_saved_activations(model, [default_input1, default_input2, default_input3])
    show_model_graph(model, [default_input1, default_input2, default_input3],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'looping_from_inputs1_unrolled'))
    show_model_graph(model, [default_input1, default_input2, default_input3],
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'looping_from_inputs1_rolled'))


def test_looping_from_inputs2(default_input1, default_input2, default_input3):
    model = example_models.LoopingFromInputs2()
    assert validate_saved_activations(model, [[default_input1, default_input2, default_input3]])
    show_model_graph(model, [[default_input1, default_input2, default_input3]],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'looping_from_inputs2_unrolled'))
    show_model_graph(model, [[default_input1, default_input2, default_input3]],
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'looping_from_inputs2_rolled'))


def test_looping_inputs_and_outputs(default_input1, default_input2, default_input3):
    model = example_models.LoopingInputsAndOutputs()
    assert validate_saved_activations(model, [[default_input1, default_input2, default_input3]])
    show_model_graph(model, [[default_input1, default_input2, default_input3]],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'looping_inputs_and_outputs_unrolled'))
    show_model_graph(model, [[default_input1, default_input2, default_input3]],
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'looping_inputs_and_outputs_rolled'))


def test_stochastic_loop(default_input1):
    model = example_models.StochasticLoop()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'stochastic_loop_unrolled'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'stochastic_loop_rolled'))


def test_recurrent_params_simple(input_2d):
    model = example_models.RecurrentParamsSimple()
    assert validate_saved_activations(model, input_2d)
    show_model_graph(model, input_2d,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'recurrent_params_simple_unrolled'))
    show_model_graph(model, input_2d,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'recurrent_params_simple_rolled'))


def test_recurrent_params_complex(input_2d):
    model = example_models.RecurrentParamsComplex()
    assert validate_saved_activations(model, input_2d)
    show_model_graph(model, input_2d,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'recurrent_params_complex_unrolled'))
    show_model_graph(model, input_2d,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'recurrent_params_complex_rolled'))


def test_looping_params_doublenested(input_2d):
    model = example_models.LoopingParamsDoubleNested()
    assert validate_saved_activations(model, input_2d)
    show_model_graph(model, input_2d,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'looping_params_doublenested_unrolled'))
    show_model_graph(model, input_2d,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'looping_params_doublenested_rolled'))


def test_module_looping_clash1(default_input1):
    model = example_models.ModuleLoopingClash1()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'module_looping_clash1_unrolled'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'module_looping_clash1_rolled'))


def test_module_looping_clash2(default_input1):
    model = example_models.ModuleLoopingClash2()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'module_looping_clash2_unrolled'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'module_looping_clash2_rolled'))


def test_module_looping_clash3(default_input1):
    model = example_models.ModuleLoopingClash3()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'module_looping_clash3_unrolled'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'module_looping_clash3_rolled'))


def test_ubermodel1(input_2d):
    model = example_models.UberModel1()
    assert validate_saved_activations(model, [[input_2d, input_2d * 2, input_2d * 3]])
    show_model_graph(model, [[input_2d, input_2d * 2, input_2d * 3]],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'ubermodel1'))


def test_ubermodel2():
    model = example_models.UberModel2()
    model_input = torch.rand(2, 1, 3, 3)
    assert validate_saved_activations(model, model_input)
    show_model_graph(model, model_input,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'ubermodel2'))


def test_ubermodel3(input_2d):
    model = example_models.UberModel3()
    assert validate_saved_activations(model, input_2d)
    show_model_graph(model, input_2d,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'ubermodel3_unrolled'))
    show_model_graph(model, input_2d,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'ubermodel3_rolled'))


def test_ubermodel4(input_2d):
    model = example_models.UberModel4()
    assert validate_saved_activations(model, input_2d)
    show_model_graph(model, input_2d,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'ubermodel4_unrolled'))
    show_model_graph(model, input_2d,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'ubermodel4_rolled'))


def test_ubermodel5():
    model = example_models.UberModel5()
    model_input = torch.rand(1, 1, 3, 3)
    assert validate_saved_activations(model, model_input)
    show_model_graph(model, model_input,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'ubermodel5'))


def test_ubermodel6(default_input1):
    model = example_models.UberModel6()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'ubermodel6_unrolled'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'ubermodel6_rolled'))


def test_ubermodel7(input_2d):
    model = example_models.UberModel7()
    assert validate_saved_activations(model, input_2d)
    show_model_graph(model, input_2d,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'ubermodel7_unrolled'))
    show_model_graph(model, input_2d,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'ubermodel7_rolled'))


def test_ubermodel8():
    model = example_models.UberModel8()
    model_input = torch.rand(2, 1, 3, 3)
    assert validate_saved_activations(model, model_input)
    show_model_graph(model, model_input,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'ubermodel8'))


def test_ubermodel9():
    model = example_models.UberModel9()
    model_input = torch.rand(1, 1, 3, 3)
    assert validate_saved_activations(model, model_input)
    show_model_graph(model, model_input,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'ubermodel9'))


# Torchvision Main Models

def test_alexnet(default_input1):
    model = torchvision.models.AlexNet()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'alexnet'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=1,
                     vis_outpath=opj('visualization_outputs', 'alexnet_depth1'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=2,
                     vis_outpath=opj('visualization_outputs', 'alexnet_depth2'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=3,
                     vis_outpath=opj('visualization_outputs', 'alexnet_depth3'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=4,
                     vis_outpath=opj('visualization_outputs', 'alexnet_depth4'))


def test_googlenet(default_input1):
    model = torchvision.models.GoogLeNet()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_buffer_layers=True,
                     vis_outpath=opj('visualization_outputs', 'googlenet_showbuffer'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_buffer_layers=False,
                     vis_outpath=opj('visualization_outputs', 'googlenet_nobuffer'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_buffer_layers=True,
                     vis_nesting_depth=1,
                     vis_outpath=opj('visualization_outputs', 'googlenet_showbuffer_depth1'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_buffer_layers=False,
                     vis_nesting_depth=1,
                     vis_outpath=opj('visualization_outputs', 'googlenet_nobuffer_depth1'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_buffer_layers=True,
                     vis_nesting_depth=2,
                     vis_outpath=opj('visualization_outputs', 'googlenet_showbuffer_depth2'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_buffer_layers=False,
                     vis_nesting_depth=2,
                     vis_outpath=opj('visualization_outputs', 'googlenet_nobuffer_depth2'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_buffer_layers=True,
                     vis_nesting_depth=3,
                     vis_outpath=opj('visualization_outputs', 'googlenet_showbuffer_depth3'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_buffer_layers=False,
                     vis_nesting_depth=3,
                     vis_outpath=opj('visualization_outputs', 'googlenet_nobuffer_depth3'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_buffer_layers=True,
                     vis_nesting_depth=4,
                     vis_outpath=opj('visualization_outputs', 'googlenet_showbuffer_depth4'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_buffer_layers=False,
                     vis_nesting_depth=4,
                     vis_outpath=opj('visualization_outputs', 'googlenet_nobuffer_depth4'))


def test_vgg16(default_input1):
    model = torchvision.models.vgg16()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'vgg16'))


def test_vgg19(default_input1):
    model = torchvision.models.vgg19()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'vgg19'))


def test_resnet50(default_input1):
    model = torchvision.models.resnet50()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'resnet50'))


def test_resnet101(default_input1):
    model = torchvision.models.resnet101()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'resnet101'))


def test_resnet152(default_input1):
    model = torchvision.models.resnet152()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'resnet152'))


def test_convnext_large(default_input1):
    model = torchvision.models.convnext_large()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'convnext'))


def test_densenet121(default_input1):
    model = torchvision.models.densenet121()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'densenet121'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=1,
                     vis_outpath=opj('visualization_outputs', 'densenet121_depth1'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=2,
                     vis_outpath=opj('visualization_outputs', 'densenet121_depth2'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=3,
                     vis_outpath=opj('visualization_outputs', 'densenet121_depth3'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=4,
                     vis_outpath=opj('visualization_outputs', 'densenet121_depth4'))


def test_efficientnet_b6(default_input1):
    model = torchvision.models.efficientnet_b6()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'efficientnet_b6'))


def test_squeezenet(default_input1):
    model = torchvision.models.squeezenet1_1()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'squeezenet'))


def test_mobilenet(default_input1):
    model = torchvision.models.mobilenet_v3_large()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'mobilenet'))


def test_wide_resnet(default_input1):
    model = torchvision.models.wide_resnet101_2()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'wide_resnet'))


def test_mnasnet(default_input1):
    model = torchvision.models.mnasnet1_3()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'mnasnet'))


def test_shufflenet(default_input1):
    model = torchvision.models.shufflenet_v2_x1_5()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'shufflenet'))


def test_resnext(default_input1):
    model = torchvision.models.resnext101_64x4d()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'resnext'))


def test_regnet(default_input1):
    model = torchvision.models.regnet_x_32gf()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'regnet'))


def test_swin_v2b(default_input1):
    model = torchvision.models.swin_v2_b()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'swin_v2b'))


def test_vit(default_input1):
    model = torchvision.models.vit_l_16()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'vit_l_16'))


def test_maxvit(default_input1):
    model = torchvision.models.maxvit_t()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'max_vit'))


def test_inception_v3():
    model = torchvision.models.inception_v3()
    model_input = torch.randn(2, 3, 299, 299)
    assert validate_saved_activations(model, model_input)
    show_model_graph(model, model_input,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'inception_v3'))


# Cornet Models

def test_cornet_s(default_input1):
    model = cornet.cornet_s()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'cornet_s_unrolled'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'cornet_s_rolled'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=1,
                     vis_outpath=opj('visualization_outputs', 'cornet_s_unrolled_depth1'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_nesting_depth=1,
                     vis_outpath=opj('visualization_outputs', 'cornet_s_rolled_depth1'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=2,
                     vis_outpath=opj('visualization_outputs', 'cornet_s_unrolled_depth2'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_nesting_depth=2,
                     vis_outpath=opj('visualization_outputs', 'cornet_s_rolled_depth2'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=3,
                     vis_outpath=opj('visualization_outputs', 'cornet_s_unrolled_depth3'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_nesting_depth=3,
                     vis_outpath=opj('visualization_outputs', 'cornet_s_rolled_depth3'))


def test_cornet_r(default_input1):
    model = cornet.cornet_r()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'cornet_r_unrolled'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'cornet_r_rolled'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=1,
                     vis_outpath=opj('visualization_outputs', 'cornet_r_unrolled_depth1'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_nesting_depth=1,
                     vis_outpath=opj('visualization_outputs', 'cornet_r_rolled_depth1'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=2,
                     vis_outpath=opj('visualization_outputs', 'cornet_r_unrolled_depth2'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_nesting_depth=2,
                     vis_outpath=opj('visualization_outputs', 'cornet_r_rolled_depth2'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=3,
                     vis_outpath=opj('visualization_outputs', 'cornet_r_unrolled_depth3'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_nesting_depth=3,
                     vis_outpath=opj('visualization_outputs', 'cornet_r_rolled_depth3'))


def test_cornet_rt():
    model = cornet.cornet_rt()
    model_input = torch.rand((6, 3, 224, 224)).to('cuda')
    assert validate_saved_activations(model, model_input)
    show_model_graph(model, model_input,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'cornet_rt_unrolled'))
    show_model_graph(model, model_input,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'cornet_rt_rolled'))
    show_model_graph(model, model_input,
                     vis_opt='unrolled',
                     vis_nesting_depth=1,
                     vis_outpath=opj('visualization_outputs', 'cornet_rt_unrolled_depth1'))
    show_model_graph(model, model_input,
                     vis_opt='rolled',
                     vis_nesting_depth=1,
                     vis_outpath=opj('visualization_outputs', 'cornet_rt_rolled_depth1'))
    show_model_graph(model, model_input,
                     vis_opt='unrolled',
                     vis_nesting_depth=2,
                     vis_outpath=opj('visualization_outputs', 'cornet_rt_unrolled_depth2'))
    show_model_graph(model, model_input,
                     vis_opt='rolled',
                     vis_nesting_depth=2,
                     vis_outpath=opj('visualization_outputs', 'cornet_rt_rolled_depth2'))
    show_model_graph(model, model_input,
                     vis_opt='unrolled',
                     vis_nesting_depth=3,
                     vis_outpath=opj('visualization_outputs', 'cornet_rt_unrolled_depth3'))
    show_model_graph(model, model_input,
                     vis_opt='rolled',
                     vis_nesting_depth=3,
                     vis_outpath=opj('visualization_outputs', 'cornet_rt_rolled_depth3'))


def test_cornet_z(default_input1):
    model = cornet.cornet_z()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'cornet_z_unrolled'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_outpath=opj('visualization_outputs', 'cornet_z_rolled'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=1,
                     vis_outpath=opj('visualization_outputs', 'cornet_z_unrolled_depth1'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_nesting_depth=1,
                     vis_outpath=opj('visualization_outputs', 'cornet_z_rolled_depth1'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=2,
                     vis_outpath=opj('visualization_outputs', 'cornet_z_unrolled_depth2'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_nesting_depth=2,
                     vis_outpath=opj('visualization_outputs', 'cornet_z_rolled_depth2'))
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_nesting_depth=3,
                     vis_outpath=opj('visualization_outputs', 'cornet_z_unrolled_depth3'))
    show_model_graph(model, default_input1,
                     vis_opt='rolled',
                     vis_nesting_depth=3,
                     vis_outpath=opj('visualization_outputs', 'cornet_z_rolled_depth3'))


# Torchvision Segmentation Models

def test_deeplabv3_mobilenet(default_input1):
    model = torchvision.models.segmentation.deeplabv3_mobilenet_v3_large()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'deeplabv3_mobilenet'))


def test_deeplabv3_resnet50(default_input1):
    model = torchvision.models.segmentation.deeplabv3_mobilenet_resnet50()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'deeplabv3_resnet50'))


def test_fcn_resnet101(default_input1):
    model = torchvision.models.segmentation.fcn_resnet101()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'fcn_resnet101'))


def test_fcn_resnet101(default_input1):
    model = torchvision.models.segmentation.fcn_resnet101()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'fcn_resnet101'))


def test_lraspp_mobilenet(default_input1):
    model = torchvision.models.segmentation.lraspp_mobilenet_v3_large()
    assert validate_saved_activations(model, default_input1)
    show_model_graph(model, default_input1,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'lraspp_mobilenet'))


# Torchvision Detection Models

def test_fasterrcnn_mobilenet_train(default_input1, default_input2):
    model = torchvision.models.detection.fasterrcnn_mobilenet_v3_large_320_fpn()
    input_tensors = [default_input1[0], default_input2[0]]
    targets = [{'boxes': torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]]), 'labels': torch.tensor([1, 2])},
               {'boxes': torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]]), 'labels': torch.tensor([1, 2])}]
    model_inputs = (input_tensors, targets)
    show_model_graph(model, model_inputs,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'fasterrcnn_mobilenet_v3_large_train'))
    assert validate_saved_activations(model, model_inputs)


def test_fasterrcnn_mobilenet_eval(default_input1, default_input2):
    model = torchvision.models.detection.fasterrcnn_mobilenet_v3_large_320_fpn()
    input_tensors = [default_input1[0], default_input2[0]]
    model = model.eval()
    show_model_graph(model, [input_tensors],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'fasterrcnn_mobilenet_v3_large_eval'))
    assert validate_saved_activations(model, [input_tensors])


def test_maskrcnn_resnet50_train(default_input1, default_input2):
    model = torchvision.models.detection.maskrcnn_resnet50_fpn()
    input_tensors = [default_input1[0], default_input2[0]]
    targets = [{'boxes': torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]]),
                'labels': torch.tensor([1, 2]),
                'masks': torch.rand(2, 224, 224).type(torch.uint8)},
               {'boxes': torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]]),
                'labels': torch.tensor([1, 2]),
                'masks': torch.rand(2, 224, 224).type(torch.uint8)}]
    model_inputs = (input_tensors, targets)
    show_model_graph(model, model_inputs,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'maskrcnn_resnet50_train'))
    assert validate_saved_activations(model, model_inputs, random_seed=0)


def test_maskrcnn_resnet50_eval(default_input1, default_input2):
    model = torchvision.models.detection.maskrcnn_resnet50_fpn()
    input_tensors = [default_input1[0], default_input2[0]]
    model = model.eval()
    show_model_graph(model, [input_tensors],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'fmaskrcnn_resnet50_eval'))
    assert validate_saved_activations(model, [input_tensors])


def test_fcos_resnet50_train(default_input1, default_input2):
    model = torchvision.models.detection.fcos_resnet50_fpn()
    input_tensors = [default_input1[0], default_input2[0]]
    targets = [{'boxes': torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]]), 'labels': torch.tensor([1, 2])},
               {'boxes': torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]]), 'labels': torch.tensor([1, 2])}]
    model_inputs = (input_tensors, targets)
    show_model_graph(model, model_inputs,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'fcos_resnet50_train'))
    assert validate_saved_activations(model, model_inputs)


def test_fcos_resnet50_eval(default_input1, default_input2):
    model = torchvision.models.detection.fcos_resnet50_fpn()
    input_tensors = [default_input1[0], default_input2[0]]
    model = model.eval()
    show_model_graph(model, [input_tensors],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'fcos_resnet50_eval'))
    assert validate_saved_activations(model, [input_tensors])


def test_retinanet_resnet50_train(default_input1, default_input2):
    model = torchvision.models.detection.retinanet_resnet50_fpn()
    input_tensors = [default_input1[0], default_input2[0]]
    targets = [{'boxes': torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]]), 'labels': torch.tensor([1, 2])},
               {'boxes': torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]]), 'labels': torch.tensor([1, 2])}]
    model_inputs = (input_tensors, targets)
    show_model_graph(model, model_inputs,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'retinanet_resnet50_train'))
    assert validate_saved_activations(model, model_inputs)


def test_retinanet_resnet50_eval(default_input1, default_input2):
    model = torchvision.models.detection.retinanet_resnet50_fpn()
    input_tensors = [default_input1[0], default_input2[0]]
    model = model.eval()
    show_model_graph(model, [input_tensors],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'retinanet_resnet50_eval'))
    assert validate_saved_activations(model, [input_tensors])


def test_ssd300_vgg16_train(default_input1, default_input2):
    model = torchvision.models.detection.ssd300_vgg16()
    input_tensors = [default_input1[0], default_input2[0]]
    targets = [{'boxes': torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]]), 'labels': torch.tensor([1, 2])},
               {'boxes': torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]]), 'labels': torch.tensor([1, 2])}]
    model_inputs = (input_tensors, targets)
    show_model_graph(model, model_inputs,
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'ssd300_vgg16_train'))
    assert validate_saved_activations(model, model_inputs)


def test_ssd300_vgg16_eval(default_input1, default_input2):
    model = torchvision.models.detection.ssd300_vgg16()
    input_tensors = [default_input1[0], default_input2[0]]
    model = model.eval()
    show_model_graph(model, [input_tensors],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'ssd300_vgg16_eval'))
    assert validate_saved_activations(model, [input_tensors])


def test_keypointrcnn_resnet50_eval(default_input1, default_input2):
    model = torchvision.models.detection.keypointrcnn_resnet50_fpn()
    input_tensors = [default_input1[0], default_input2[0]]
    model = model.eval()
    show_model_graph(model, [input_tensors],
                     vis_opt='unrolled',
                     vis_outpath=opj('visualization_outputs', 'keypointrcnn_resnet50_eval'),
                     save_only=True)
    assert validate_saved_activations(model, [input_tensors])
