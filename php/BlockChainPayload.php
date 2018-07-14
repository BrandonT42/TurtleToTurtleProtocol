<?php
// Copyright (c) 2018, The TurtleCoin Developers
// 
// Please see the included LICENSE file for more information.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Turtle2Turtle.proto

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>BlockChainPayload</code>
 */
class BlockChainPayload extends \Google\Protobuf\Internal\Message
{
    protected $data;

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type \TurtleBlock $block
     *     @type \TurtleTransaction $transaction
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Turtle2Turtle::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>.TurtleBlock block = 1;</code>
     * @return \TurtleBlock
     */
    public function getBlock()
    {
        return $this->readOneof(1);
    }

    /**
     * Generated from protobuf field <code>.TurtleBlock block = 1;</code>
     * @param \TurtleBlock $var
     * @return $this
     */
    public function setBlock($var)
    {
        GPBUtil::checkMessage($var, \TurtleBlock::class);
        $this->writeOneof(1, $var);

        return $this;
    }

    /**
     * Generated from protobuf field <code>.TurtleTransaction transaction = 2;</code>
     * @return \TurtleTransaction
     */
    public function getTransaction()
    {
        return $this->readOneof(2);
    }

    /**
     * Generated from protobuf field <code>.TurtleTransaction transaction = 2;</code>
     * @param \TurtleTransaction $var
     * @return $this
     */
    public function setTransaction($var)
    {
        GPBUtil::checkMessage($var, \TurtleTransaction::class);
        $this->writeOneof(2, $var);

        return $this;
    }

    /**
     * @return string
     */
    public function getData()
    {
        return $this->whichOneof("data");
    }

}

