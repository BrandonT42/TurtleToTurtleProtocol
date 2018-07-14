// Copyright (c) 2018, The TurtleCoin Developers
// 
// Please see the included LICENSE file for more information.

/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

goog.provide('proto.T2TDatagram');

goog.require('jspb.BinaryReader');
goog.require('jspb.BinaryWriter');
goog.require('jspb.Message');
goog.require('proto.BlockChainPayload');
goog.require('proto.T2TCandidateList');
goog.require('proto.T2TCandidateListRequest');


/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.T2TDatagram = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, proto.T2TDatagram.oneofGroups_);
};
goog.inherits(proto.T2TDatagram, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.T2TDatagram.displayName = 'proto.T2TDatagram';
}
/**
 * Oneof group definitions for this message. Each group defines the field
 * numbers belonging to that group. When of these fields' value is set, all
 * other fields in the group are cleared. During deserialization, if multiple
 * fields are encountered for a group, only the last value seen will be kept.
 * @private {!Array<!Array<number>>}
 * @const
 */
proto.T2TDatagram.oneofGroups_ = [[4,5,6]];

/**
 * @enum {number}
 */
proto.T2TDatagram.DatapayloadCase = {
  DATAPAYLOAD_NOT_SET: 0,
  T2TCANDIDATELIST: 4,
  T2TCANDIDATELISTREQUEST: 5,
  BLOCKCHAINPAYLOAD: 6
};

/**
 * @return {proto.T2TDatagram.DatapayloadCase}
 */
proto.T2TDatagram.prototype.getDatapayloadCase = function() {
  return /** @type {proto.T2TDatagram.DatapayloadCase} */(jspb.Message.computeOneofCase(this, proto.T2TDatagram.oneofGroups_[0]));
};



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.T2TDatagram.prototype.toObject = function(opt_includeInstance) {
  return proto.T2TDatagram.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.T2TDatagram} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.T2TDatagram.toObject = function(includeInstance, msg) {
  var f, obj = {
    p2pnetworkid: jspb.Message.getFieldWithDefault(msg, 1, 0),
    version: jspb.Message.getFieldWithDefault(msg, 2, 0),
    peerid: jspb.Message.getFieldWithDefault(msg, 3, ""),
    t2tcandidatelist: (f = msg.getT2tcandidatelist()) && proto.T2TCandidateList.toObject(includeInstance, f),
    t2tcandidatelistrequest: (f = msg.getT2tcandidatelistrequest()) && proto.T2TCandidateListRequest.toObject(includeInstance, f),
    blockchainpayload: (f = msg.getBlockchainpayload()) && proto.BlockChainPayload.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.T2TDatagram}
 */
proto.T2TDatagram.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.T2TDatagram;
  return proto.T2TDatagram.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.T2TDatagram} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.T2TDatagram}
 */
proto.T2TDatagram.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readUint32());
      msg.setP2pnetworkid(value);
      break;
    case 2:
      var value = /** @type {number} */ (reader.readUint32());
      msg.setVersion(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setPeerid(value);
      break;
    case 4:
      var value = new proto.T2TCandidateList;
      reader.readMessage(value,proto.T2TCandidateList.deserializeBinaryFromReader);
      msg.setT2tcandidatelist(value);
      break;
    case 5:
      var value = new proto.T2TCandidateListRequest;
      reader.readMessage(value,proto.T2TCandidateListRequest.deserializeBinaryFromReader);
      msg.setT2tcandidatelistrequest(value);
      break;
    case 6:
      var value = new proto.BlockChainPayload;
      reader.readMessage(value,proto.BlockChainPayload.deserializeBinaryFromReader);
      msg.setBlockchainpayload(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.T2TDatagram.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.T2TDatagram.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.T2TDatagram} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.T2TDatagram.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getP2pnetworkid();
  if (f !== 0) {
    writer.writeUint32(
      1,
      f
    );
  }
  f = message.getVersion();
  if (f !== 0) {
    writer.writeUint32(
      2,
      f
    );
  }
  f = message.getPeerid();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = message.getT2tcandidatelist();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      proto.T2TCandidateList.serializeBinaryToWriter
    );
  }
  f = message.getT2tcandidatelistrequest();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      proto.T2TCandidateListRequest.serializeBinaryToWriter
    );
  }
  f = message.getBlockchainpayload();
  if (f != null) {
    writer.writeMessage(
      6,
      f,
      proto.BlockChainPayload.serializeBinaryToWriter
    );
  }
};


/**
 * optional uint32 p2pNetworkId = 1;
 * @return {number}
 */
proto.T2TDatagram.prototype.getP2pnetworkid = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/** @param {number} value */
proto.T2TDatagram.prototype.setP2pnetworkid = function(value) {
  jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional uint32 version = 2;
 * @return {number}
 */
proto.T2TDatagram.prototype.getVersion = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/** @param {number} value */
proto.T2TDatagram.prototype.setVersion = function(value) {
  jspb.Message.setProto3IntField(this, 2, value);
};


/**
 * optional string peerId = 3;
 * @return {string}
 */
proto.T2TDatagram.prototype.getPeerid = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/** @param {string} value */
proto.T2TDatagram.prototype.setPeerid = function(value) {
  jspb.Message.setProto3StringField(this, 3, value);
};


/**
 * optional T2TCandidateList t2tCandidateList = 4;
 * @return {?proto.T2TCandidateList}
 */
proto.T2TDatagram.prototype.getT2tcandidatelist = function() {
  return /** @type{?proto.T2TCandidateList} */ (
    jspb.Message.getWrapperField(this, proto.T2TCandidateList, 4));
};


/** @param {?proto.T2TCandidateList|undefined} value */
proto.T2TDatagram.prototype.setT2tcandidatelist = function(value) {
  jspb.Message.setOneofWrapperField(this, 4, proto.T2TDatagram.oneofGroups_[0], value);
};


proto.T2TDatagram.prototype.clearT2tcandidatelist = function() {
  this.setT2tcandidatelist(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.T2TDatagram.prototype.hasT2tcandidatelist = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional T2TCandidateListRequest t2tCandidateListRequest = 5;
 * @return {?proto.T2TCandidateListRequest}
 */
proto.T2TDatagram.prototype.getT2tcandidatelistrequest = function() {
  return /** @type{?proto.T2TCandidateListRequest} */ (
    jspb.Message.getWrapperField(this, proto.T2TCandidateListRequest, 5));
};


/** @param {?proto.T2TCandidateListRequest|undefined} value */
proto.T2TDatagram.prototype.setT2tcandidatelistrequest = function(value) {
  jspb.Message.setOneofWrapperField(this, 5, proto.T2TDatagram.oneofGroups_[0], value);
};


proto.T2TDatagram.prototype.clearT2tcandidatelistrequest = function() {
  this.setT2tcandidatelistrequest(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.T2TDatagram.prototype.hasT2tcandidatelistrequest = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * optional BlockChainPayload blockChainPayload = 6;
 * @return {?proto.BlockChainPayload}
 */
proto.T2TDatagram.prototype.getBlockchainpayload = function() {
  return /** @type{?proto.BlockChainPayload} */ (
    jspb.Message.getWrapperField(this, proto.BlockChainPayload, 6));
};


/** @param {?proto.BlockChainPayload|undefined} value */
proto.T2TDatagram.prototype.setBlockchainpayload = function(value) {
  jspb.Message.setOneofWrapperField(this, 6, proto.T2TDatagram.oneofGroups_[0], value);
};


proto.T2TDatagram.prototype.clearBlockchainpayload = function() {
  this.setBlockchainpayload(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.T2TDatagram.prototype.hasBlockchainpayload = function() {
  return jspb.Message.getField(this, 6) != null;
};


